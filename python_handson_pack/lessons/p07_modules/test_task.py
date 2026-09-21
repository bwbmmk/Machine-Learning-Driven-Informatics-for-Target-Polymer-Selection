import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p07_modules import task
from support import DATA, read_fixture


class ModuleTests(unittest.TestCase):
    def test_pipeline(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary = task.run_pipeline(DATA/'teaching_records.json', Path(tmp)/'out')
            self.assertEqual(summary['kept'], 6)
            self.assertEqual(summary['input_count'], 12)
            self.assertTrue((Path(tmp)/'out'/'cleaned.csv').exists())
    def test_root_object_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                task.run_pipeline(DATA/'wrong_root.json', Path(tmp)/'out')
            self.assertFalse((Path(tmp)/'out').exists())
    def test_import_has_no_file_writes(self):
        import importlib
        from unittest.mock import patch
        with patch('builtins.open', side_effect=AssertionError('import must not open data')), patch('pathlib.Path.open', side_effect=AssertionError('import must not open data')):
            importlib.reload(task)
