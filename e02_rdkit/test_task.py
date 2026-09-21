import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.e02_rdkit import task
from support import DATA, read_fixture


import importlib.util

@unittest.skipUnless(importlib.util.find_spec('rdkit'), 'Install rdkit for E02')
class RDKitTests(unittest.TestCase):
    def test_simple(self):
        result=task.describe_smiles('CCO')
        self.assertIs(result['valid'],True)
        self.assertEqual(result['num_atoms'],3)
        self.assertEqual(result['num_rings'],0)
        self.assertGreater(result['mol_wt'],0)
    def test_ring(self):
        result=task.describe_smiles('c1ccccc1')
        self.assertEqual(result['num_atoms'],6)
        self.assertEqual(result['num_rings'],1)
    def test_invalid(self):
        expected={'valid':False,'num_atoms':None,'mol_wt':None,'num_rings':None}
        for value in [None,'','   ','not_a_smiles']:
            self.assertEqual(task.describe_smiles(value),expected)
