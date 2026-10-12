import unittest
import pandas as pd
from scripts.audit_executed_contributions import reconstruct

class ExecutedContributionTests(unittest.TestCase):
    def fixtures(self):
        dates=pd.to_datetime(['2026-01-02','2026-01-05','2026-01-06'])
        prices=pd.DataFrame({'A':[10.,11.,12.], 'B':[20.,18.,19.]},index=dates)
        events=[{'date':dates[0],'before':{},'cash_before':1.,'after':{'A':.5},'cash_after':.49,'fee':.01},
                {'date':dates[1],'before':{'A':.55},'cash_before':.49,'after':{'B':.72},'cash_after':.30,'fee':.02}]
        equity=pd.DataFrame({'date':[dates[0],dates[1],dates[2]],'nav':[1.,1.02,1.06]})
        return prices,events,equity
    def test_executed_switch_cost_and_cash_reconstruct_nav(self):
        prices,events,equity=self.fixtures()
        daily,stocks,audit=reconstruct(prices,events,equity,'2026-01-06')
        self.assertTrue(audit['passed'])
        self.assertAlmostEqual(float(stocks[stocks.ts_code=='A'].pnl.sum()),.05)
        self.assertAlmostEqual(float(stocks[stocks.ts_code=='B'].pnl.sum()),.04)
        self.assertAlmostEqual(float(daily.fee.sum()),.03)
        self.assertAlmostEqual(float(daily.iloc[-1].nav),1.06)
    def test_wrong_actual_positions_fail_closed(self):
        prices,events,equity=self.fixtures();events[1]['before']['A']=.56
        with self.assertRaises(ValueError):reconstruct(prices,events,equity,'2026-01-06')
    def test_nav_mismatch_fails_closed(self):
        prices,events,equity=self.fixtures();equity.loc[2,'nav']=1.07
        with self.assertRaises(ValueError):reconstruct(prices,events,equity,'2026-01-06')
    def test_future_prices_do_not_change_past(self):
        prices,events,equity=self.fixtures()
        a,_,_=reconstruct(prices,events,equity,'2026-01-05')
        prices.iloc[2]=[999.,999.]
        b,_,_=reconstruct(prices,events,equity,'2026-01-05')
        pd.testing.assert_frame_equal(a,b)

class LinkedContributionTests(unittest.TestCase):
    def test_comparison_reconstructs_log_nav_difference(self):
        import tempfile
        from pathlib import Path
        from scripts.audit_executed_contributions import compare_contributions
        prices,events,equity=ExecutedContributionTests().fixtures()
        a,stocks,_=reconstruct(prices,events,equity,'2026-01-06')
        with tempfile.TemporaryDirectory() as tmp:
            paths=[Path(tmp)/'a',Path(tmp)/'b']
            for p in paths:
                p.mkdir();a.to_csv(p/'executed_daily_nav.csv',index=False);stocks.to_csv(p/'executed_stock_contributions.csv',index=False)
            comparison=compare_contributions(*paths)
            self.assertAlmostEqual(comparison['net_log_return_delta'],0.)
            self.assertAlmostEqual(comparison['reconciliation_residual'],0.)
