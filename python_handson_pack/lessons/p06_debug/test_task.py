import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p06_debug import task
from support import DATA, read_fixture


class DebugTests(unittest.TestCase):
    def test_offset(self):
        self.assertAlmostEqual(task.c_to_k(12), 285.15)
    def test_duplicates(self):
        rows = [{'record_id':'a'},{'record_id':'b'},{'record_id':'a'}]
        self.assertEqual(task.find_all(rows,'a'), [rows[0],rows[2]])
        self.assertEqual(task.find_all(rows,'x'), [])
    def test_empty_mean(self):
        self.assertIsNone(task.mean_or_none([]))
        self.assertEqual(task.mean_or_none([2,4,9]), 5)
