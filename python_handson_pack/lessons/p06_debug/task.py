"""下面是故意有缺陷的程序。先写测试重现，再修复。"""

def c_to_k(value):
    return value + 273  # BUG: 请用手算例子定位

def find_all(records, key):
    for row in records:
        if row['record_id'] == key:
            return row  # BUG: 返回值与重复情况
    return None

def mean_or_none(values):
    return sum(values) / len(values)  # BUG: 边界输入
