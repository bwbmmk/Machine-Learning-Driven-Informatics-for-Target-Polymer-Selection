"""P01 练习骨架：读取教学记录。TODO 部分需要由你完成。"""

import json
from pathlib import Path


# 相对脚本定位数据，避免工作目录变化导致找不到文件。
DATA_PATH = Path(__file__).resolve().parent / "data" / "teaching_records.json"


def load_records(path):
    """读取 UTF-8 JSON 文件，返回由记录字典组成的列表。"""
    # TODO：使用 with 打开 path，再用 json.load 读取并返回数据。
    raise NotImplementedError("请先完成 load_records(path)")


def main():
    # TODO：调用 load_records(DATA_PATH)。
    # TODO：打印总条数。
    # TODO：逐条打印前 3 条的 record_id、name、tg_value、tg_unit。
    raise NotImplementedError("请完成读取、计数和展示逻辑")


if __name__ == "__main__":
    main()
