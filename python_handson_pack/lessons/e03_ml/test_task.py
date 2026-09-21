import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.e03_ml import task
from support import DATA, read_fixture


import importlib.util

@unittest.skipUnless(importlib.util.find_spec('sklearn'), 'Install scikit-learn for E03')
class MLTests(unittest.TestCase):
    def test_metrics_and_split(self):
        rows=read_fixture('toy_regression.json')
        old=copy.deepcopy(rows)
        result=task.train_and_evaluate(rows)
        self.assertEqual(result['n_train'],48)
        self.assertEqual(result['n_test'],12)
        self.assertEqual(len(result['train_ids']),48)
        self.assertEqual(len(result['test_ids']),12)
        self.assertFalse(set(result['train_ids']) & set(result['test_ids']))
        self.assertEqual(set(result['train_ids']) | set(result['test_ids']), {r['record_id'] for r in rows})
        self.assertEqual(rows,old)
        # 独立核算基线，防止直接编造指标或偷用测试标签均值。
        from sklearn.model_selection import train_test_split
        train,test=train_test_split(rows,test_size=0.2,random_state=42)
        self.assertEqual(result['test_ids'],[r['record_id'] for r in test])
        avg=sum(r['target'] for r in train)/len(train)
        expected=math.sqrt(sum((r['target']-avg)**2 for r in test)/len(test))
        self.assertAlmostEqual(result['baseline_rmse'],expected,places=7)
        self.assertTrue(math.isfinite(result['model_rmse']))
        self.assertGreaterEqual(result['model_rmse'],0)
    def test_repeat_and_invalid(self):
        rows=read_fixture('toy_regression.json')
        a=task.train_and_evaluate(rows)
        b=task.train_and_evaluate(rows)
        self.assertAlmostEqual(a['model_rmse'],b['model_rmse'])
        with self.assertRaises(ValueError): task.train_and_evaluate(rows[:3])
        with self.assertRaises(ValueError): task.train_and_evaluate(rows+[rows[0]])
