import csv
import json
from pathlib import Path
from lessons.p03_units.task import to_kelvin
from lessons.p04_validate.task import validate_record

def clean_records(records):
    raise NotImplementedError('TODO: 清洗并返回全部行日志')

def save_bundle(cleaned, logs, output_dir):
    raise NotImplementedError('TODO: 导出四个文件，保护已有输出')
