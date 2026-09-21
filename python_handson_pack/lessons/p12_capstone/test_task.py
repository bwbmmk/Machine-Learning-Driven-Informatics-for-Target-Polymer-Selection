import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.p12_capstone import task
from support import DATA, read_fixture


import contextlib
import io

class CapstoneTests(unittest.TestCase):
    def test_selection_order(self):
        rows=[{'record_id':'a','name':'Alpha','tg_k':310.0},{'record_id':'b','name':'Beta','tg_k':340.0},{'record_id':'c','name':'ALPHABET','tg_k':330.0}]
        old=copy.deepcopy(rows)
        self.assertEqual([r['record_id'] for r in task.select_records(rows,'alpha',300,340,1)],['c'])
        self.assertEqual(len(task.select_records(rows,'  ',300,350,10)),3)
        self.assertEqual(task.select_records(rows,'missing',300,350,10),[])
        self.assertEqual(rows,old)
    def test_real_job(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            summary=task.run_job(DATA/'teaching_records.json',out,'demo',300,350,2)
            self.assertEqual(summary,{'input_count':12,'kept':6,'selected':2})
            selected=json.loads((out/'selected.json').read_text(encoding='utf-8'))
            self.assertEqual([r['record_id'] for r in selected],['EX11','EX10'])
            self.assertTrue((out/'rejected.csv').exists())
            self.assertEqual(json.loads((out/'selection_summary.json').read_text(encoding='utf-8')),summary)
    def test_preflight(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'bad'
            with self.assertRaises(ValueError): task.run_job(DATA/'teaching_records.json',out,'',4,2,1)
            self.assertFalse(out.exists())
            out.mkdir()
            (out/'selected.json').write_text('KEEP',encoding='utf-8')
            with self.assertRaises(FileExistsError): task.run_job(DATA/'teaching_records.json',out,'',1,999,3)
            self.assertEqual([p.name for p in out.iterdir()],['selected.json'])
    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            buf=io.StringIO()
            with contextlib.redirect_stdout(buf):
                code=task.main(['--input',str(DATA/'teaching_records.json'),'--output-dir',str(Path(tmp)/'cli'),'--low','300','--high','350','--top','2'])
            self.assertEqual(code,0)
            self.assertEqual(json.loads(buf.getvalue())['selected'],2)
