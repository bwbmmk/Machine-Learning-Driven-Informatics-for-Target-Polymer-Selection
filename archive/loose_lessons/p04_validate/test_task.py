import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p04_validate import task
from support import DATA, read_fixture


class ValidateTests(unittest.TestCase):
    def test_fixture_counts(self):
        report = task.check_records(read_fixture())
        self.assertEqual(len(report), 12)
        self.assertEqual(sum(r['ok'] for r in report), 7)
        self.assertEqual([r['record_id'] for r in report if not r['ok']], ['EX04','EX05','EX06','EX07','EX08'])
        self.assertEqual([r['row_number'] for r in report], list(range(1,13)))
    def test_multi_error_and_shape(self):
        self.assertGreaterEqual(len(task.validate_record({'tg_value': 'bad', 'tg_unit': 'K'})), 2)
        self.assertTrue(task.validate_record(None))
        self.assertEqual(task.check_records([]), [])
        r = task.check_records([None])[0]
        self.assertEqual(set(r), {'row_number','record_id','ok','errors'})
        self.assertIsNone(r['record_id'])
        self.assertIs(r['ok'], False)
        self.assertTrue(all(isinstance(x, str) and x for x in r['errors']))
    def test_optional_fields_and_no_mutation(self):
        row = {'record_id':'new', 'tg_value':20, 'tg_unit':'C', 'smiles':'bad'}
        old = copy.deepcopy(row)
        self.assertEqual(task.validate_record(row), [])
        self.assertEqual(row, old)
