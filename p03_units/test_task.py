import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p03_units import task
from support import DATA, read_fixture


class UnitTests(unittest.TestCase):
    def test_valid(self):
        for value, unit, expected in [(25,'C',298.15),('-20',' c ',253.15),(310,'K',310.0),(0,'C',273.15)]:
            with self.subTest(value=value, unit=unit):
                result = task.to_kelvin(value, unit)
                self.assertIsInstance(result, float)
                self.assertAlmostEqual(result, expected)
    def test_invalid(self):
        pairs = [(None,'C'),(True,'C'),('', 'C'),('warm','C'),('nan','K'),('inf','K'),(0,'K'),(-300,'C'),(5,'F'),(5,None),([], 'K')]
        for value, unit in pairs:
            with self.subTest(value=value, unit=unit):
                with self.assertRaises(ValueError):
                    task.to_kelvin(value, unit)
    def test_roundtrip(self):
        for c in [-100.0, 0.0, 37.5, 500.0]:
            self.assertAlmostEqual(task.kelvin_to_celsius(task.to_kelvin(c,'C')), c)
        with self.assertRaises(ValueError):
            task.kelvin_to_celsius(0)
