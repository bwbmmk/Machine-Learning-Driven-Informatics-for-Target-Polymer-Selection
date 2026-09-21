import csv
from pathlib import Path
from lessons.p03_units.task import to_kelvin

def adapt_rows(rows, source_name):
    raise NotImplementedError('TODO: 字段映射与明确类型转换')

def read_provider(path, source_name):
    raise NotImplementedError('TODO: CSV 读取与适配')
