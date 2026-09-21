import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p10_pandas import task
from support import DATA, read_fixture


import importlib.util

@unittest.skipUnless(importlib.util.find_spec('pandas'), 'Install pandas for P10')
class PandasTests(unittest.TestCase):
    def test_strings_and_order(self):
        rows=[{'record_id':'a','tg_k':'300'},{'record_id':'b','tg_k':'350'},{'record_id':'c','tg_k':'350'},{'record_id':'d','tg_k':'400'}]
        old=copy.deepcopy(rows)
        result=task.dataframe_report(rows,300,350,3)
        self.assertEqual(result['filtered_ids'],['a','b','c'])
        self.assertEqual(result['top_ids'],['d','b','c'])
        self.assertEqual(result['stats'],{'count':4,'min':300.0,'max':400.0,'mean':350.0})
        self.assertEqual(rows,old)
    def test_empty_and_invalid(self):
        result=task.dataframe_report([],1,2,2)
        self.assertEqual(result,{'filtered_ids':[],'top_ids':[],'stats':{'count':0,'min':None,'max':None,'mean':None}})
        for rows,lo,hi,n in [([],2,1,1),([],1,2,-1),([{'record_id':'x','tg_k':'bad'}],1,2,1),([{'record_id':'x','tg_k':'nan'}],1,2,1)]:
            with self.assertRaises(ValueError): task.dataframe_report(rows,lo,hi,n)
