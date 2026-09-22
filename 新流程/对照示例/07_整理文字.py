# 对照示例：先写自己的程序并运行，再打开此文件。
raw_unit = " c "
name = "Sample_Alpha"
keyword = "ALPHA"
unit = raw_unit.strip().upper()
matches = keyword.lower() in name.lower()
print(f"单位：{unit}")
print(f"名字包含关键词：{matches}")
