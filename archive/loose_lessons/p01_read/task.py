"""P01：你负责读取和预览逻辑。"""
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / 'data' / 'teaching_records.json'

def load_records(path):
    raise NotImplementedError('TODO: 读取 JSON')

def preview_records(records, n=3):
    raise NotImplementedError('TODO: 返回前 n 条')

def main():
    raise NotImplementedError('TODO: 调用上述函数并打印结果')

if __name__ == '__main__':
    main()
