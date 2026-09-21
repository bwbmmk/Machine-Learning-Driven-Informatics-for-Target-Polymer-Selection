from datetime import datetime
import hashlib
from pathlib import Path

def failed_counts(events, start, end):
    raise NotImplementedError('TODO: 时间过滤和失败次数')

def sha256_file(path):
    raise NotImplementedError('TODO: 分块读取并计算摘要')
