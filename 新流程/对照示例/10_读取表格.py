# 对照示例：先写自己的程序并运行，再打开此文件。
import csv
from pathlib import Path

base = Path(__file__).resolve().parents[1]
source = base / "data" / "mini_polymers.csv"
with source.open("r", encoding="utf-8", newline="") as file:
    records = list(csv.DictReader(file))
for record in records[:2]:
    print(record["record_id"], record["name"])
print(f"共 {len(records)} 条")
