# 对照示例：先写自己的程序并运行，再打开此文件。
records = [
    {"record_id": "A01", "name": "alpha", "tg_value": 25},
    {"record_id": "A02", "name": "beta", "tg_value": 310},
    {"record_id": "A03", "name": "gamma", "tg_value": -20},
]
wanted_id = "A02"
found = False
for record in records:
    if record["record_id"] == wanted_id:
        print(f"找到了：{record['name']}")
        found = True
if not found:
    print("没有找到")
