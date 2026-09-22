# 对照示例：先写自己的程序并运行，再打开此文件。
import json
from pathlib import Path

base = Path(__file__).resolve().parents[1]
source = base / "output" / "cleaned.json"
with source.open("r", encoding="utf-8") as file:
    records = json.load(file)
selected = [row for row in records if 300 <= row["tg_k"] <= 350]
selected = sorted(selected, key=lambda row: row["tg_k"], reverse=True)
for row in selected:
    print(f"{row['record_id']} {row['tg_k']} K")
