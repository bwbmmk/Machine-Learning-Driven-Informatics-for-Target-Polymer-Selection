import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.e04_security import task
from support import DATA, read_fixture


class SecurityTests(unittest.TestCase):
    def test_counts_and_boundaries(self):
        rows=read_fixture('synthetic_events.json')
        self.assertEqual(task.failed_counts(rows,'2026-01-01T00:00:00+00:00','2026-01-01T01:00:00+00:00'),{'demo_u1':2,'demo_u2':1})
        self.assertEqual(task.failed_counts([], '2026-01-01T00:00:00+00:00','2026-01-01T01:00:00+00:00'),{})
        with self.assertRaises(ValueError): task.failed_counts([], '2026-01-02T00:00:00+00:00','2026-01-01T00:00:00+00:00')
        with self.assertRaises(ValueError): task.failed_counts([], '2026-01-01T00:00:00','2026-01-02T00:00:00')
    def test_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'sample.bin'
            p.write_bytes(b'abc')
            self.assertEqual(task.sha256_file(p),'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
            old=task.sha256_file(p)
            p.write_bytes(b'abcd')
            self.assertNotEqual(task.sha256_file(p),old)
            with self.assertRaises(FileNotFoundError): task.sha256_file(Path(tmp)/'absent')
