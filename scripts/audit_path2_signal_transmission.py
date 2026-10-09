#!/usr/bin/env python3
"""隔离重放 Path2 的实际排序、晋升门槛、状态及目标；不修改策略逻辑。"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import inspect
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import backtest_marketcap_etf as engine

PARENT_VARIANT = 'aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn'
GATE_ABLATION_VARIANT = 'aggr_03_97_prom3_liqmom_gate_mom61_off_20261010'


def register_gate_ablation():
    """只在显式隔离进程中注册，正式研究池不增长。"""
    parent = next(v for v in engine.WINNER_CORE_VARIANTS if v['variant_id'] == PARENT_VARIANT)
    engine.WINNER_CORE_VARIANTS.append({
        **parent, 'variant_id': GATE_ABLATION_VARIANT,
        'variant_name': '冻结v63，仅移除标准与快速晋升的重复6-1硬门槛',
        'standard_promotion_min_momentum_6_1_rank': 0.,
        'fast_promotion_min_momentum_6_1_rank': 0.,
        'alpha_pool_profile': engine.ALPHA_POOL_PROFILE_GROWTH_ELASTIC,
    })


def finite_map(series):
    return {str(k): float(v) for k, v in series.items() if math.isfinite(float(v))}


def promotion_gates(local):
    """逐门槛验算必须与引擎实际集合一致，否则终止审计。"""
    ranks = local['satellite_signal_ranks']
    index = ranks.index
    standard = {
        'rank': ranks >= local['standard_promotion_rank_threshold'],
        'industry_strength': local['industry_strength_scores'].reindex(index).fillna(0) >= local['standard_promotion_min_industry_strength'],
        'industry_leader': local['industry_leader_scores'].reindex(index).fillna(0) >= local['standard_promotion_min_industry_leader'],
        'momentum_6_1': local['promotion_momentum_6_1_rank'] >= local['standard_promotion_min_momentum_6_1_rank'],
        'momentum_3_1': local['promotion_momentum_3_1_rank'] >= local['standard_promotion_min_momentum_3_1_rank'],
    }
    fast = {
        'rank': ranks >= ranks.quantile(1 - local['fast_promotion_percentile']),
        'industry_strength': local['industry_strength_scores'].reindex(index).fillna(0) >= local['fast_promotion_min_industry_strength'],
        'industry_leader': local['industry_leader_scores'].reindex(index).fillna(0) >= local['fast_promotion_min_industry_leader'],
        'momentum_6_1': local['promotion_momentum_6_1_rank'] >= local['fast_promotion_min_momentum_6_1_rank'],
        'momentum_3_1': local['promotion_momentum_3_1_rank'] >= local['fast_promotion_min_momentum_3_1_rank'],
        'breakout': local['breakout_signal'].reindex(index).fillna(False).astype(bool),
        'recent_return': local['recent_1m_returns'].reindex(index).fillna(-1) > local['fast_promotion_min_recent_1m_return'],
        'amount_surge': local['amount_surge_ratio'].reindex(index).fillna(0) >= local['fast_promotion_min_amount_surge_ratio'],
    }
    result = {}
    for name, gates in [('standard', standard), ('fast', fast)]:
        mask = engine.pd.Series(True, index=index)
        for gate in gates.values():
            mask &= gate
        actual = set(local[name + '_promotion_candidates'])
        if set(mask[mask].index) != actual:
            raise RuntimeError('审计门槛与引擎实际集合不一致：' + name)
        result[name] = {
            'pass_codes': {key: sorted(map(str, gate[gate].index)) for key, gate in gates.items()},
            'candidates': sorted(map(str, actual)),
        }
    return result


def synthetic_checks():
    """无门槛饱和时排序可改变选择；全候选晋升时排序可被门槛压扁。"""
    pd = engine.pd
    scores = [pd.Series({'A': 0.9, 'B': 0.1}), pd.Series({'A': 0.1, 'B': 0.9})]
    chosen = []
    saturated = []
    for score in scores:
        weights, _ = engine.build_single_sleeve_weights(
            base_weights=pd.Series({'A': 1., 'B': 1.}), signal_scores=score,
            recent_1m_returns=pd.Series({'A': .1, 'B': .1}),
            quality_scores=pd.Series({'A': 1., 'B': 1.}), currently_held_codes=set(),
            target_exposure=1., buy_entry_percentile=.5, sell_exit_percentile=1.,
            quality_quantile=0., max_holdings=1, base_weight_mode='signal',
        )
        chosen.append(sorted(weights.index))
        candidates = set(score[score >= score.quantile(0.)].index)
        state = engine.update_promoted_core_state(
            promoted_core_codes=set(), promoted_core_ages={},
            promotion_streaks={c: engine.PROMOTION_MIN_STREAK - 1 for c in candidates},
            demotion_streaks={}, standard_promotion_candidates=candidates,
            core_selected_codes=candidates,
            avg_daily_amount=pd.Series({c: engine.CORE_AMOUNT_THRESHOLD * 2 for c in candidates}),
            actual_core_members=set(), fast_promotion_candidates=set(),
        )
        saturated.append(sorted(state[0]))
    assert chosen == [['A'], ['B']], chosen
    assert saturated == [['A', 'B'], ['A', 'B']], saturated
    return {'unconstrained_selection': chosen, 'saturated_promotion_state': saturated, 'passed': True}


def summarize_trace(path, candidate, parent):
    records = {}
    completion = None
    synthetic = None
    fields = ['promoted_before', 'promoted_after', 'raw_target_weights', 'capped_target_weights', 'core_selected_codes']
    with gzip.open(path, 'rt', encoding='utf-8') as handle:
        for line in handle:
            row = json.loads(line)
            if row.get('type') == 'completion':
                completion = row
                continue
            if row.get('type') == 'synthetic_checks':
                synthetic = row
                continue
            if row['strategy_base_id'] not in {candidate, parent}:
                continue
            compact = {k: row[k] for k in fields}
            for k in ['promotion_scores', 'core_signal_scores']:
                compact[k] = hashlib.sha256(json.dumps(row[k], sort_keys=True).encode()).hexdigest()
            compact['gates'] = {k: row['gates'][k]['candidates'] for k in ['standard', 'fast']}
            compact['promoted_inputs'] = {
                code: {
                    'core_score': row['core_signal_scores'].get(code),
                    'daily_amount': row.get('avg_daily_amount', {}).get(code),
                    'seed_eligible': code in row['seed_eligible_codes'] if 'seed_eligible_codes' in row else None,
                    'actual_core_member': code in row['actual_core_members'] if 'actual_core_members' in row else None,
                    'target_weight': row['raw_target_weights'].get(code, 0.),
                    'protected_keep': code in row.get('selection_stats', {}).get('core_protected_keep_candidates', []) if 'selection_stats' in row else None,
                } for code in row['promoted_before']
            }
            records[(row['sample_tag'], row['strategy_base_id'], row['signal_date'])] = compact
    if completion is None or not synthetic or not synthetic['passed']:
        raise RuntimeError('审计未完成或合成验收缺失')
    windows = {}
    tags = sorted({key[0] for key in records})
    for tag in tags:
        dates = sorted(key[2] for key in records if key[:2] == (tag, candidate))
        parent_dates = sorted(key[2] for key in records if key[:2] == (tag, parent))
        if not dates or dates != parent_dates:
            raise RuntimeError('对照信号日不一致：' + tag)
        pairs = [(d, records[(tag, candidate, d)], records[(tag, parent, d)]) for d in dates]
        windows[tag] = {
            'signal_dates': len(dates),
            'different_days': {k: sum(a[k] != b[k] for _, a, b in pairs) for k in fields + ['promotion_scores', 'core_signal_scores']},
            'candidate_set_different_days': {k: sum(a['gates'][k] != b['gates'][k] for _, a, b in pairs) for k in ['standard', 'fast']},
            'max_target_weight_difference': max((abs(a['capped_target_weights'].get(c, 0.) - b['capped_target_weights'].get(c, 0.)) for _, a, b in pairs for c in a['capped_target_weights'].keys() | b['capped_target_weights'].keys()), default=0.),
            'changed_state_examples': [
                {'signal_date': d, 'different_codes': sorted(set(a['promoted_before']) ^ set(b['promoted_before'])),
                 'candidate_inputs': {c: a['promoted_inputs'].get(c) for c in set(a['promoted_before']) ^ set(b['promoted_before'])},
                 'parent_inputs': {c: b['promoted_inputs'].get(c) for c in set(a['promoted_before']) ^ set(b['promoted_before'])},
                 'target_equal': a['raw_target_weights'] == b['raw_target_weights']}
                for d, a, b in pairs if a['promoted_before'] != b['promoted_before']
            ][:5],
        }
    return {'candidate_id': candidate, 'parent_id': parent, 'windows': windows,
            'completion': completion, 'synthetic_checks': synthetic,
            'trace_path': str(Path(path).resolve()), 'trace_sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-jsonl-gz', type=Path)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--gate-ablation', action='store_true', help='显式注册单项门槛消融；仅写隔离comparison')
    parser.add_argument('--summarize', type=Path, help='汇总既有审计，不重复回测')
    parser.add_argument('--candidate-id')
    parser.add_argument('--parent-id')
    parser.add_argument('--summary-json', type=Path)
    parser.add_argument('--audit-signal-dates', default='', help='只记录指定诊断日；回测仍运行显式窗口')
    parser.add_argument('--inspect-codes', default='', help='记录指定证券的质量与短期收益门槛')
    args, forwarded = parser.parse_known_args()
    if args.self_test:
        print(json.dumps(synthetic_checks(), ensure_ascii=False))
        return
    if args.summarize:
        if not args.candidate_id or not args.parent_id or not args.summary_json:
            parser.error('汇总必须指定candidate-id、parent-id、summary-json')
        summary = summarize_trace(args.summarize, args.candidate_id, args.parent_id)
        args.summary_json.parent.mkdir(parents=True, exist_ok=True)
        args.summary_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
        print('已汇总', len(summary['windows']), '窗口：', args.summary_json)
        return
    if args.output_jsonl_gz is None or '--only-base-ids' not in forwarded or '--comparison-csv' not in forwarded or '--end-date' not in forwarded:
        parser.error('必须显式指定隔离输出、only-base-ids、comparison-csv及end-date')
    ids = set(forwarded[forwarded.index('--only-base-ids') + 1].split(','))
    if len(ids) > 3 or not all(i.startswith('core_explore_70_30_equal_weight_winner_core') for i in ids):
        parser.error('仅支持最多三个冻结Path2配置')
    if args.gate_ablation:
        comparison = Path(forwarded[forwarded.index('--comparison-csv') + 1]).resolve()
        official = (ROOT / 'results/research/a_share').resolve()
        if comparison.is_relative_to(official):
            parser.error('消融comparison必须位于正式研究comparison目录之外')
        if not any(i.endswith('__' + GATE_ABLATION_VARIANT) for i in ids):
            parser.error('gate-ablation必须显式选择消融ID')
        register_gate_ablation()
    args.output_jsonl_gz.parent.mkdir(parents=True, exist_ok=True)
    original = engine.update_promoted_core_state
    cash_original = engine.compute_rebalance_trades
    cash_calls = 0
    audit_dates = set(filter(None, args.audit_signal_dates.split(',')))
    inspect_codes = set(filter(None, args.inspect_codes.split(',')))
    with gzip.open(args.output_jsonl_gz, 'wt', encoding='utf-8') as output:
        output.write(json.dumps({'type': 'synthetic_checks', **synthetic_checks()}, ensure_ascii=False) + '\n')

        def audited_state(**kwargs):
            local = inspect.currentframe().f_back.f_locals
            config = local['strategy_config']
            if config['strategy_base_id'] not in ids:
                raise RuntimeError('审计出现未指定配置')
            gates = promotion_gates(local)
            before_codes = sorted(map(str, kwargs['promoted_core_codes']))
            before_ages = dict(kwargs['promoted_core_ages'])
            state = original(**kwargs)
            if audit_dates and str(local['signal_date'].date()) not in audit_dates:
                return state
            record = {
                'strategy_base_id': config['strategy_base_id'], 'sample_tag': config['sample_tag'],
                'signal_date': str(local['signal_date'].date()),
                'promotion_scores': finite_map(local['satellite_signal_ranks']), 'gates': gates,
                'promoted_before': before_codes, 'ages_before': before_ages,
                'promoted_after': sorted(map(str, state[0])), 'ages_after': state[1],
                'promotion_streaks_after': state[2], 'status': state[4],
                'core_selected_codes': sorted(map(str, kwargs['core_selected_codes'])),
                'raw_target_weights': finite_map(local['raw_target_weights']),
                'capped_target_weights': finite_map(local['target_weights']),
                'target_cash_weight': float(local['target_cash_weight']),
                'core_signal_scores': finite_map(local['core_signal_scores']),
                'actual_core_members': sorted(map(str, local['actual_core_members'])),
                'actual_explore_members': sorted(map(str, local['actual_explore_members'])),
                'seed_eligible_codes': sorted(map(str, local['seed_eligible_codes'])),
                'avg_daily_amount': finite_map(local['avg_daily_amount']),
                'selection_stats': {k: sorted(map(str, v)) if isinstance(v, set) else v for k, v in local['selection_stats'].items()},
                'inspected_codes': {code: {
                    'quality_score': finite_map(local['quality_scores'].reindex([code])).get(code),
                    'recent_1m_return': finite_map(local['recent_1m_returns'].reindex([code])).get(code),
                    'promoted_before': code in before_codes,
                    'seed_eligible': code in local['seed_eligible_codes'],
                    'avg_daily_amount': finite_map(local['avg_daily_amount'].reindex([code])).get(code),
                } for code in sorted(inspect_codes)},
                'note': '本次目标使用promoted_before；promoted_after在后续信号日消费',
            }
            output.write(json.dumps(record, ensure_ascii=False, allow_nan=False) + '\n')
            return state

        def audited_cash(*a, **kw):
            nonlocal cash_calls
            positions, cash, gross_positions, gross_cash, stats = cash_original(*a, **kw)
            nav = float(positions.sum() + cash)
            if cash < -max(nav, 1.) * 1e-9 or (nav > 0 and float(positions.sum()) / nav > 1 + 1e-9):
                raise RuntimeError('资金恒等式边界失败')
            cash_calls += 1
            gross_nav = float(gross_positions.sum() + gross_cash)
            if gross_cash < -max(gross_nav, 1.) * 1e-9:
                raise RuntimeError('gross资金边界失败')
            return positions, cash, gross_positions, gross_cash, stats

        engine.update_promoted_core_state = audited_state
        engine.compute_rebalance_trades = audited_cash
        try:
            engine.main(forwarded)
            output.write(json.dumps({'type': 'completion', 'cash_calls': cash_calls, 'capital_violations': 0}) + '\n')
        finally:
            engine.update_promoted_core_state = original
            engine.compute_rebalance_trades = cash_original


if __name__ == '__main__':
    main()
