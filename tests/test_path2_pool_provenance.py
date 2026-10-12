import unittest
import pandas as pd
from scripts.path2_candidate_pass import _filter_growth_elastic_rows

class PoolProvenanceTests(unittest.TestCase):
    def test_cross_pool_and_missing_provenance_excluded(self):
        frame=pd.DataFrame({'strategy_base_id':['core','growth','unknown'],'pool_id':['core_explore_seed','growth_elastic',None]})
        self.assertEqual(_filter_growth_elastic_rows(frame).strategy_base_id.tolist(),['growth'])
    def test_conflicting_profile_excluded(self):
        frame=pd.DataFrame({'pool_id':['growth_elastic','growth_elastic'],'alpha_pool_profile':['core_explore_seed','growth_elastic']})
        self.assertEqual(_filter_growth_elastic_rows(frame).index.tolist(),[1])
    def test_no_pool_column_fails_closed(self):
        self.assertTrue(_filter_growth_elastic_rows(pd.DataFrame({'strategy_base_id':['x']})).empty)
