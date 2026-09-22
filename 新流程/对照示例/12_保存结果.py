# 对照示例：先写自己的程序并运行，再打开此文件。
import csv
import json
from pathlib import Path


def clean_rows(rows):
    cleaned = []
    seen_ids = set()
    for row in rows:
        record_id = row["record_id"]
        if record_id in seen_ids:
            continue
        try:
            value = float(row["tg_value"])
        except ValueError:
            continue
        unit = row["tg_unit"].strip().upper()
        if unit == "C":
            kelvin = value + 273.15
        elif unit == "K":
            kelvin = value
        else:
            continue
        if kelvin <= 0:
            continue
        new_row = row.copy()
        new_row["tg_k"] = round(kelvin, 2)
        cleaned.append(new_row)
        seen_ids.add(record_id)
    return cleaned


base = Path(__file__).resolve().parents[1]
with (base / "data" / "mini_polymers.csv").open("r", encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))
cleaned = clean_rows(rows)
output = base / "output"
output.mkdir(exist_ok=True)
with (output / "cleaned.json").open("w", encoding="utf-8") as file:
    json.dump(cleaned, file, ensure_ascii=False, indent=2)
print(f"已保存 {len(cleaned)} 条到 output/cleaned.json")
