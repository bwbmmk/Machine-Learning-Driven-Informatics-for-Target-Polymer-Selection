import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p11_plot import task
from support import DATA, read_fixture


import importlib.util

@unittest.skipUnless(importlib.util.find_spec('matplotlib'), 'Install matplotlib for P11')
class PlotTests(unittest.TestCase):
    def test_outputs(self):
        rows=[{'record_id':'a','tg_k':300.0},{'record_id':'b','tg_k':330.0},{'record_id':'c','tg_k':380.0}]
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'figures'
            paths=task.make_plots(rows,out)
            self.assertEqual([Path(p).name for p in paths],['histogram.png','by_id.png'])
            for p in paths:
                self.assertEqual(Path(p).read_bytes()[:8],bytes([137,80,78,71,13,10,26,10]))
                self.assertGreater(Path(p).stat().st_size,500)
            with self.assertRaises(FileExistsError): task.make_plots(rows,out)
    def test_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'empty'
            self.assertEqual(task.make_plots([],out),[])
            self.assertFalse(out.exists())
