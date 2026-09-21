import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p05_clean import task
from support import DATA, read_fixture


import csv

class CleanTests(unittest.TestCase):
    def test_fixture(self):
        rows = read_fixture()
        old = copy.deepcopy(rows)
        clean, logs = task.clean_records(rows)
        self.assertEqual([r['record_id'] for r in clean], ['EX01','EX02','EX03','EX09','EX10','EX11'])
        self.assertEqual(rows, old)
        self.assertEqual(len(logs), 12)
        self.assertEqual(sum(r['status']=='invalid' for r in logs), 5)
        self.assertEqual(logs[10]['status'], 'duplicate')
        self.assertAlmostEqual(clean[0]['tg_k'], 298.15)
        self.assertTrue(all(r['is_synthetic'] for r in clean))
    def test_conflict_and_invalid_first(self):
        a = {'record_id':'x', 'tg_value':20, 'tg_unit':'C'}
        bad = dict(a, tg_value='bad')
        other = dict(a, tg_value=30)
        clean, logs = task.clean_records([bad, a, dict(a), other])
        self.assertEqual([r['status'] for r in logs], ['invalid','kept','duplicate','duplicate_conflict'])
        self.assertEqual(len(clean), 1)
        for row in logs:
            self.assertEqual(set(row), {'row_number','record_id','status','reason'})
            if row['status'] != 'kept': self.assertTrue(row['reason'])
    def test_export_and_no_overwrite(self):
        clean, logs = task.clean_records(read_fixture())
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'new'
            task.save_bundle(clean, logs, out)
            self.assertEqual(json.loads((out/'cleaned.json').read_text(encoding='utf-8')), clean)
            summary = json.loads((out/'summary.json').read_text(encoding='utf-8'))
            self.assertEqual(summary, dict(input_count=12, kept=6, invalid=5, duplicate=1, duplicate_conflict=0))
            with (out/'cleaned.csv').open(encoding='utf-8-sig', newline='') as f:
                self.assertEqual(len(list(csv.DictReader(f))), 6)
            with (out/'rejected.csv').open(encoding='utf-8-sig', newline='') as f:
                self.assertEqual(len(list(csv.DictReader(f))), 6)
            before = {p.name:p.read_bytes() for p in out.iterdir()}
            with self.assertRaises(FileExistsError): task.save_bundle(clean, logs, out)
            self.assertEqual(before, {p.name:p.read_bytes() for p in out.iterdir()})
    def test_empty_export(self):
        self.assertEqual(task.clean_records([]), ([], []))
        with tempfile.TemporaryDirectory() as tmp:
            task.save_bundle([], [], tmp)
            with (Path(tmp)/'cleaned.csv').open(encoding='utf-8-sig', newline='') as f:
                reader = csv.DictReader(f)
                self.assertIn('tg_k', reader.fieldnames)
                self.assertEqual(list(reader), [])
