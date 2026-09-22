# 对照示例：先写自己的程序并运行，再打开此文件。
from pathlib import Path

base = Path(__file__).resolve().parents[1]
source = base / "data" / "mini_polymers.csv"
with source.open("r", encoding="utf-8", newline="") as file:
    next(file)  # 略过表头
    count = 0
    for line in file:
        count += 1
print(f"表格中有 {count} 条原始资料")
