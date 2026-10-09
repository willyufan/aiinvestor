import copy
import unittest

from scripts import audit_path2_signal_transmission as audit


class SignalTransmissionAuditTests(unittest.TestCase):
    def test_distinguishes_signal_consumption_from_saturated_state(self):
        result = audit.synthetic_checks()
        self.assertTrue(result['passed'])
        self.assertNotEqual(*result['unconstrained_selection'])
        self.assertEqual(*result['saturated_promotion_state'])

    def test_gate_audit_fails_closed_on_engine_mismatch(self):
        pd = audit.engine.pd
        ranks = pd.Series({'A': .9, 'B': .1})
        local = {'satellite_signal_ranks': ranks, 'standard_promotion_rank_threshold': .5,
                 'fast_promotion_percentile': .5,
                 'industry_strength_scores': ranks, 'industry_leader_scores': ranks,
                 'promotion_momentum_6_1_rank': ranks, 'promotion_momentum_3_1_rank': ranks,
                 'breakout_signal': pd.Series({'A': True, 'B': True}),
                 'recent_1m_returns': ranks, 'amount_surge_ratio': ranks,
                 'standard_promotion_candidates': {'A'}, 'fast_promotion_candidates': {'A'}}
        for kind in ['standard', 'fast']:
            for field in ['industry_strength', 'industry_leader', 'momentum_6_1_rank', 'momentum_3_1_rank']:
                local[kind + '_promotion_min_' + field] = 0.
        local['fast_promotion_min_recent_1m_return'] = 0.
        local['fast_promotion_min_amount_surge_ratio'] = 0.
        self.assertEqual(audit.promotion_gates(local)['standard']['candidates'], ['A'])
        local['standard_promotion_candidates'] = {'B'}
        with self.assertRaisesRegex(RuntimeError, '不一致'):
            audit.promotion_gates(local)

    def test_ablation_freezes_parent_and_changes_only_two_gates(self):
        variants = audit.engine.WINNER_CORE_VARIANTS
        before = copy.deepcopy(variants)
        try:
            audit.register_gate_ablation()
            parent = next(v for v in variants if v['variant_id'] == audit.PARENT_VARIANT)
            candidate = variants[-1]
            differences = {k for k in parent.keys() | candidate.keys() if parent.get(k) != candidate.get(k)}
            self.assertEqual(differences, {'variant_id', 'variant_name', 'alpha_pool_profile',
                                          'standard_promotion_min_momentum_6_1_rank',
                                          'fast_promotion_min_momentum_6_1_rank'})
            self.assertEqual(variants[:-1], before)
            self.assertNotIn(candidate['variant_id'], audit.engine.PATH2_SCAN_VARIANT_IDS)
        finally:
            variants[:] = before


if __name__ == '__main__':
    unittest.main()
