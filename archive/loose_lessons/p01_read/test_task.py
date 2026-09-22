import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p01_read import task
from support import DATA, read_fixture


class ReadTests(unittest.TestCase):
    def test_read_real_file(self):
        rows = task.load_records(DATA / 'teaching_records.json')
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows[0]['record_id'], 'EX01')
    def test_arbitrary_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'other.json'
            p.write_text('[{"record_id": "新输入"}]', encoding='utf-8')
            self.assertEqual(task.load_records(str(p)), [{'record_id': '新输入'}])
    def test_preview_boundaries(self):
        rows = [{'a': 1}, {'a': 2}]
        before = copy.deepcopy(rows)
        self.assertEqual(task.preview_records(rows, 1), rows[:1])
        self.assertEqual(task.preview_records(rows, 0), [])
        self.assertEqual(task.preview_records(rows, 99), rows)
        self.assertEqual(rows, before)
        with self.assertRaises(ValueError):
            task.preview_records(rows, -1)
    def test_empty_and_bad_json(self):
        self.assertEqual(task.load_records(DATA / 'empty.json'), [])
        with self.assertRaises(json.JSONDecodeError):
            task.load_records(DATA / 'malformed.json')
