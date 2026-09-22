# E01 数据导入与来源记录

前置：P08；选做。知识：CSV、字段映射、可追溯性。

## 你要亲手做的步骤

1. 先用包内 provider_sample.csv 练导入，它是纯教学数据。
2. 写 adapt_rows 将另一家提供方的列名映射成练习格式。
3. 单位转换复用 P03，目标字段保存为 tg_value（K）和 tg_unit='K'。
4. 整理 SOURCE_NOTES.md，日后换真实数据时再核查来源和表示。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

adapt_rows(rows, source_name) -> 标准字典列表。输入列 sample_id、label、temperature、unit、structure、is_synthetic；教学 CSV 的 is_synthetic 是字符串 true/false，不区分大小写；未知值抛 ValueError，不能默认为真实。
输出 record_id、name、smiles、tg_value（K浮点）、tg_unit='K'、is_synthetic（bool）、source（source_name）。不修改输入。不合法温度或空 ID 抛 ValueError，先不做隔离表。
read_provider(path, source_name) 用 csv.DictReader 并调用 adapt_rows。
实际转接真实数据时，source_name 不是来源证据的替代；本题只教转换，真实数据还需附原始出处、单位依据和许可。

## 验收命令

在练习包根目录运行：

```powershell
py check.py E01
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

增加一份不同列名的教学表，用配置字典指定列映射；实际真实数据由你后续选择，本包没有伪造实验来源。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

写清教学来源与真实来源的区别，不能因字段转换成功就认定数据科学有效。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
