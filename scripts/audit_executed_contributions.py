#!/usr/bin/env python3
"""隔离重放并以实际成交后持仓重构逐日股票贡献；不改变策略或正式产物。"""
from __future__ import annotations
import argparse
import inspect
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def reconstruct(prices, events, equity, end_date):
    """收盘成交：当日收益来自成交前持仓，成交费用独立扣除。"""
    if not events:
        raise ValueError('没有实际执行记录')
    event_dates = [pd.Timestamp(e['date']) for e in events]
    if event_dates != sorted(event_dates):
        raise ValueError('成交日期倒序')
    by_date = {}
    for e in events:
        by_date.setdefault(pd.Timestamp(e['date']), []).append(e)
    units = pd.Series(dtype=float)
    cash, previous_nav = 1., 1.
    previous_prices = None
    rows, contributions, errors = [], [], []
    checkpoints = equity.copy()
    checkpoints['date'] = pd.to_datetime(checkpoints.date)
    # 引擎初始1.0是成交前锚点，首日成交后NAV不能拿它作期末验收。
    checkpoints = checkpoints.iloc[1:].set_index('date')['nav']
    for date, price in prices.loc[event_dates[0]:pd.Timestamp(end_date)].iterrows():
        pnl = pd.Series(dtype=float) if previous_prices is None else units * (price.reindex(units.index) - previous_prices.reindex(units.index))
        if pnl.isna().any():
            raise ValueError('实际持仓价格缺失')
        cost = 0.
        for e in by_date.get(date, []):
            expected = units * price.reindex(units.index)
            incoming = pd.Series(e['before'], dtype=float)
            union = expected.index.union(incoming.index)
            position_error = float((expected.reindex(union, fill_value=0.) - incoming.reindex(union, fill_value=0.)).abs().max()) if len(union) else 0.
            errors.extend([position_error, abs(cash-e['cash_before'])])
            after = pd.Series(e['after'], dtype=float)
            delta_nav = float(incoming.sum()+e['cash_before']-after.sum()-e['cash_after'])
            errors.append(abs(delta_nav-e['fee']))
            if e['fee'] < -1e-12 or e['cash_after'] < -1e-8:
                raise ValueError('资金或费用违规')
            units = after / price.reindex(after.index)
            if not np.isfinite(units).all():
                raise ValueError('无效成交后数量')
            cash = e['cash_after']
            cost += e['fee']
        nav = float((units*price.reindex(units.index)).sum()+cash)
        residual = nav-previous_nav-float(pnl.sum())+cost
        errors.append(abs(residual))
        if date in checkpoints.index:
            errors.append(abs(nav-float(checkpoints.loc[date])))
        for code, value in pnl.items():
            contributions.append({'date':date,'ts_code':code,'pnl':float(value), 'return_contribution':float(value)/previous_nav})
        rows.append({'date':date,'nav':nav,'stock_pnl':float(pnl.sum()),'fee':cost,'cash':cash,'stock_exposure':(nav-cash)/nav,'residual':residual})
        previous_nav, previous_prices = nav, price
    maximum = max(errors, default=0.)
    if maximum > 1e-6:
        raise ValueError(f'净NAV或实际持仓验收失败：最大误差{maximum}')
    return pd.DataFrame(rows), pd.DataFrame(contributions), {'max_absolute_error':maximum,'trade_calls':len(events),'days':len(rows),'checkpoint_count':len(checkpoints),'passed':True}



def compare_contributions(candidate_dir, reference_dir):
    """对数链接贡献可加总；共有/独有指当天实际持仓，不作入口因果推断。"""
    frames, fees, logs, daily_frames = [], [], [], []
    for directory in [candidate_dir, reference_dir]:
        daily = pd.read_csv(directory / 'executed_daily_nav.csv')
        stocks = pd.read_csv(directory / 'executed_stock_contributions.csv')
        previous = daily.nav.shift(fill_value=1.)
        returns = daily.nav / previous - 1.
        link = np.log1p(returns) / returns.replace(0., 1.)
        link.loc[returns == 0.] = 1.
        daily['link'] = link
        daily['starting_exposure'] = (previous - daily.cash.shift(fill_value=1.)) / previous
        daily['stock_return'] = daily.stock_pnl / previous
        daily['sleeve_return'] = daily.stock_return / daily.starting_exposure.replace(0., 1.)
        daily_frames.append(daily)
        stocks = stocks.merge(daily[['date', 'link']], on='date', validate='many_to_one')
        stocks['log_contribution'] = stocks.return_contribution * stocks.link
        frames.append(stocks)
        fees.append(float((-daily.fee / previous * link).sum()))
        logs.append(float(np.log(daily.nav.iloc[-1])))
    if not daily_frames[0].date.equals(daily_frames[1].date):
        raise ValueError('逐日NAV日期不一致')
    a, b = daily_frames
    average_link = (a.link + b.link) / 2.
    exposure = average_link * (a.starting_exposure-b.starting_exposure) * (a.sleeve_return+b.sleeve_return) / 2.
    sleeve = average_link * (a.sleeve_return-b.sleeve_return) * (a.starting_exposure+b.starting_exposure) / 2.
    linking = (a.link-b.link) * (a.stock_return+b.stock_return) / 2.
    decomposition = {'exposure_log_delta':float(exposure.sum()), 'sleeve_return_log_delta':float(sleeve.sum()), 'linking_log_delta':float(linking.sum())}
    merged = frames[0].merge(frames[1], on=['date','ts_code'], how='outer', suffixes=('_candidate','_reference'), indicator=True, validate='one_to_one')
    merged['delta'] = merged.log_contribution_candidate.fillna(0.) - merged.log_contribution_reference.fillna(0.)
    groups = {str(k):float(v) for k,v in merged.groupby('_merge', observed=True).delta.sum().items()}
    fee_delta = fees[0]-fees[1]
    residual = logs[0]-logs[1]-float(merged.delta.sum())-fee_delta
    if abs(residual) > 1e-6:
        raise ValueError('股票与费用贡献不能重构净对数收益差')
    ranked = merged.groupby('ts_code').delta.sum().sort_values()
    return {'net_log_return_delta':logs[0]-logs[1], 'fee_log_delta':fee_delta,
            'cohort_log_delta':groups, 'reconciliation_residual':residual,
            'symmetric_exposure_decomposition':decomposition,
            'worst_five_stock_deltas':ranked.head(5).to_dict(),
            'best_five_stock_deltas':ranked.tail(5).to_dict(),
            'interpretation':'共有/独有是实际执行持仓集合；描述性分解不能识别入口或退出的因果效应'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--market', choices=['ashare','hkconnect'],required=True)
    parser.add_argument('--only-base-ids',default='')
    parser.add_argument('--only-strategy-ids',default='')
    parser.add_argument('--sample-tags',required=True)
    parser.add_argument('--end-date',required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    output=args.output_dir.resolve()
    if not output.is_relative_to(ROOT/'results/research'):
        raise ValueError('必须输出到隔离research目录')
    output.mkdir(parents=True,exist_ok=True)
    if args.market=='ashare':
        import backtest_marketcap_etf as engine
        run_name='run_backtest'; ids=args.only_base_ids;flag='--only-base-ids'
    else:
        import backtest_hkconnect as engine
        run_name='run_hk_backtest';ids=args.only_strategy_ids;flag='--only-strategy-ids'
    if not ids:
        raise ValueError('必须显式指定候选ID')
    original_run=getattr(engine,run_name)
    original_trade=engine.compute_rebalance_trades
    signature=inspect.signature(original_trade)
    context={}; audits={}
    def trade(*a,**kw):
        bound=signature.bind(*a,**kw);bound.apply_defaults();b=bound.arguments
        result=original_trade(*a,**kw)
        if context.get('active'):
            context['events'].append({'date':str(b['rebalance_date']),'before':b['current_values'].to_dict(),'cash_before':float(b['current_cash']),'after':result[0].to_dict(),'cash_after':float(result[1]),'fee':float(result[4]['trading_cost'])})
        return result
    def run(prepared,config):
        sid=str(config.get('strategy_base_id') or config.get('strategy_id'))
        tag=str(config.get('sample_tag'))
        context.update(active=True,events=[])
        try:
            result=original_run(prepared,config)
        finally:
            context['active']=False
        directory=output/(sid+'__'+tag);directory.mkdir(parents=True,exist_ok=True)
        daily, stocks, audit=reconstruct(prepared.price_ffill,context['events'],result[0],args.end_date)
        (directory/'executed_trades.json').write_text(json.dumps(context['events'],ensure_ascii=False,allow_nan=False)+'\n')
        daily.to_csv(directory/'executed_daily_nav.csv',index=False)
        stocks.to_csv(directory/'executed_stock_contributions.csv',index=False)
        audits[sid+'__'+tag]=audit
        (output/'contribution_audit.json').write_text(json.dumps(audits,ensure_ascii=False,indent=2)+'\n')
        return result
    engine.compute_rebalance_trades=trade
    setattr(engine,run_name,run)
    engine.build_output_dir=lambda sid,tag: output/(sid+'__'+tag)
    if args.market=='ashare':
        engine.build_pool_output_dir=engine.build_output_dir
    if args.market=='ashare':
        engine.main(['--end-date',args.end_date,'--sample-tags',args.sample_tags,flag,ids,'--comparison-csv',str(output/'comparison.csv')])
    else:
        original_file=engine.research_file
        engine.research_file=lambda name,**kw: output/name if name=='strategy_comparison_hkconnect.csv' else original_file(name,**kw)
        sys.argv=[sys.argv[0],'--end-date',args.end_date,'--sample-tags',args.sample_tags,flag,ids]
        engine.main()
    expected=len(ids.split(','))*len(args.sample_tags.split(','))
    if len(audits)!=expected:
        raise ValueError(f'实跑窗口不足：{len(audits)}/{expected}')

if __name__=='__main__':
    main()
