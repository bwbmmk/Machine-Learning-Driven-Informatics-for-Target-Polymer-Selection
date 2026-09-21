import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p09_stats import task
from support import DATA, read_fixture


class StatsTests(unittest.TestCase):
    def setUp(self):
        self.rows = [{'record_id':'a','tg_k':300.0},{'record_id':'b','tg_k':350.0},{'record_id':'c','tg_k':350.0},{'record_id':'d','tg_k':400.0}]
    def test_boundaries(self):
        old = copy.deepcopy(self.rows)
        self.assertEqual(task.filter_range(self.rows,300,350), self.rows[:3])
        self.assertEqual(task.filter_range(self.rows,1,2), [])
        with self.assertRaises(ValueError): task.filter_range(self.rows,3,2)
        self.assertEqual(self.rows,old)
    def test_ranking(self):
        old = copy.deepcopy(self.rows)
        self.assertEqual([r['record_id'] for r in task.top_n(self.rows,3)], ['d','b','c'])
        self.assertEqual(task.top_n(self.rows,0), [])
        self.assertEqual(len(task.top_n(self.rows,99)),4)
        with self.assertRaises(ValueError): task.top_n(self.rows,-1)
        self.assertEqual(self.rows,old)
    def test_summary(self):
        self.assertEqual(task.summarize(self.rows), {'count':4,'min':300.0,'max':400.0,'mean':350.0})
        self.assertEqual(task.summarize([]), {'count':0,'min':None,'max':None,'mean':None})
