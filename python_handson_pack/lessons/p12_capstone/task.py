import argparse
import json
import sys
from pathlib import Path
# TODO: 从前面的关卡导入需要的函数，避免复制实现。

def select_records(records, keyword, low, high, n):
    raise NotImplementedError('TODO: 按约定顺序筛选与排名')

def run_job(input_path, output_dir, keyword, low, high, n):
    raise NotImplementedError('TODO: 完整小工具，六个输出文件')

def main(argv=None):
    raise NotImplementedError('TODO: CLI 参数与反馈')

if __name__ == '__main__':
    raise SystemExit(main())
