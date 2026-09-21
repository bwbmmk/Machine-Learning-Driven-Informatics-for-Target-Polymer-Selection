# 教学输入清单

所有记录由人工或确定性公式构造，用来练程序，不是实测材料数据。

| 文件 | 用途 |
|---|---|
| teaching_records.json | 主线12行数据：7行格式/数值合法，5行失败，去重后6行 |
| empty.json | 合法空列表，与损坏文件不同 |
| wrong_root.json | JSON合法但根对象不是列表 |
| malformed.json | 故意损坏的JSON，解析失败是预期 |
| provider_sample.csv | E01字段映射用的另一种教学格式 |
| smiles_examples.json | E02简单结构字符串，非真实聚合物属性配对 |
| toy_regression.json | E03的60条数值教学数据，target不是Tg |
| synthetic_events.json | E04虚构用户的本地日志，带时区 |

主线数据的温度、名称和SMILES不构成真实性质关系。原始数据不要直接改动；独立变式用你自己的新文件。
