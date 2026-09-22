# 对照示例：先写自己的程序并运行，再打开此文件。
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description="按温度范围挑选教学资料")
parser.add_argument("--low", type=float, required=True, help="最低温度，单位 K")
parser.add_argument("--high", type=float, required=True, help="最高温度，单位 K")
args = parser.parse_args()
if args.low > args.high:
    parser.error("最低温度不能高于最高温度")

base = Path(__file__).resolve().parents[1]
with (base / "output" / "cleaned.json").open("r", encoding="utf-8") as file:
    records = json.load(file)
selected = [row for row in records if args.low <= row["tg_k"] <= args.high]
selected = sorted(selected, key=lambda row: row["tg_k"], reverse=True)
for row in selected:
    print(f"{row['record_id']} {row['tg_k']} K")
