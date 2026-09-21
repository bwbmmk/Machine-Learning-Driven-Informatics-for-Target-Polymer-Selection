import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p08_cli import task
from support import DATA, read_fixture


import contextlib
import io
import subprocess
import sys
from support import ROOT

class CLITests(unittest.TestCase):
    def test_success_and_preview(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)/'out'
            args = ['--input',str(DATA/'teaching_records.json'),'--output-dir',str(out)]
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(task.main(args+['--preview']), 0)
            self.assertEqual(json.loads(stream.getvalue())['kept'], 6)
            self.assertFalse(out.exists())
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(task.main(args), 0)
            self.assertTrue((out/'summary.json').exists())
    def test_bad_inputs(self):
        for filename in ['absent.json','malformed.json','wrong_root.json']:
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                err = io.StringIO()
                with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
                    code = task.main(['--input',str(DATA/filename),'--output-dir',str(Path(tmp)/'out')])
                self.assertEqual(code, 2)
                self.assertTrue(err.getvalue().strip())
    def test_subprocess_help_and_exit(self):
        result = subprocess.run([sys.executable,'-m','lessons.p08_cli.task','--help'],cwd=str(ROOT),capture_output=True,timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertIn(b'--input', result.stdout)
        result = subprocess.run([sys.executable,'-m','lessons.p08_cli.task','--input','missing.json','--output-dir','output/x'],cwd=str(ROOT),capture_output=True,timeout=10)
        self.assertEqual(result.returncode, 2)
