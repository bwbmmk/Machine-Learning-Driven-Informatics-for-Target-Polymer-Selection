"""Provided runner: check one lesson, prerequisites, or list the route."""
import argparse
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parent

def main(argv=None):
    parser=argparse.ArgumentParser(description='Check handwritten exercise code. Unfinished stubs are expected to fail.')
    parser.add_argument('lesson',nargs='?',help='P01..P12 or E01..E04')
    parser.add_argument('--list',action='store_true')
    parser.add_argument('--through',action='store_true',help='Run P01 through the selected P lesson')
    args=parser.parse_args(argv)
    items=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    index={row['id']:row for row in items}
    if args.list:
        for row in items: print(row['id']+'  '+row['title']+'  ['+row['folder']+']')
        return 0
    code=(args.lesson or '').upper()
    if code not in index: parser.error('Choose P01..P12 or E01..E04, or use --list')
    if args.through and not code.startswith('P'): parser.error('--through applies only to P lessons')
    selected=[row for row in items if row['id'].startswith('P') and row['id']<=code] if args.through else [index[code]]
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    for row in selected:
        module=row['folder'].replace('/','.')
        suite.addTests(loader.loadTestsFromName(module+'.test_task'))
        if row['id']=='P06': suite.addTests(loader.loadTestsFromName(module+'.test_student'))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    if result.skipped:
        print('INCOMPLETE: skipped checks (usually missing optional dependencies). This is not a pass.')
    if not result.wasSuccessful():
        print('NOT FINISHED: use the first traceback, lesson contract and HINTS.md. Unfilled TODOs should fail.')
    elif not result.skipped:
        print('AUTOMATED CHECKS PASSED. Also complete the manual review and independent variation.')
    return 0 if result.wasSuccessful() and not result.skipped else 1

if __name__=='__main__':
    raise SystemExit(main())
