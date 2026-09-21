"""已提供的练习基础设施：定位测试数据，不实现任何学习任务。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'

def read_fixture(name='teaching_records.json'):
    with (DATA / name).open(encoding='utf-8') as stream:
        return json.load(stream)
