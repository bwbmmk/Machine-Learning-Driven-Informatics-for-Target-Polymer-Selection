import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.e01_import import task
from support import DATA, read_fixture


class ImportTests(unittest.TestCase):
    def test_file(self):
        rows=task.read_provider(DATA/'provider_sample.csv','teaching-provider')
        self.assertEqual(len(rows),3)
        self.assertAlmostEqual(rows[0]['tg_value'],298.15)
        self.assertEqual(rows[0]['tg_unit'],'K')
        self.assertTrue(rows[0]['is_synthetic'])
        self.assertEqual(rows[0]['source'],'teaching-provider')
    def test_no_mutation_and_boolean(self):
        row={'sample_id':'q','label':'Demo','temperature':'310','unit':'K','structure':'CC','is_synthetic':'false'}
        old=copy.deepcopy(row)
        result=task.adapt_rows([row],'test')[0]
        self.assertIs(result['is_synthetic'],False)
        self.assertEqual(row,old)
        with self.assertRaises(ValueError): task.adapt_rows([dict(row,is_synthetic='unknown')],'test')
    def test_empty(self):
        self.assertEqual(task.adapt_rows([],'x'),[])
