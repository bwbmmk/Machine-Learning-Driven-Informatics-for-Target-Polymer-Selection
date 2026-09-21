import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p02_query import task
from support import DATA, read_fixture


class QueryTests(unittest.TestCase):
    def test_duplicate_and_missing(self):
        rows = read_fixture()
        self.assertEqual(len(task.find_by_id(rows, 'EX02')), 2)
        self.assertEqual(task.find_by_id(rows, 'absent'), [])
    def test_new_input_order_and_no_mutation(self):
        rows = [{'record_id': 'q', 'v': 2}, {'record_id': 'z'}, {'record_id': 'q', 'v': 1}]
        old = copy.deepcopy(rows)
        self.assertEqual(task.find_by_id(rows, 'q'), [rows[0], rows[2]])
        self.assertEqual(rows, old)
    def test_names(self):
        rows = [{'name': 'Alpha_X'}, {}, {'name': None}, {'name': 8}, {'name': 'xALPHA'}]
        self.assertEqual(task.search_by_name(rows, ' alpha '), [rows[0], rows[4]])
        self.assertEqual(task.search_by_name(rows, '  '), [])
        self.assertEqual(task.search_by_name([], 'a'), [])
