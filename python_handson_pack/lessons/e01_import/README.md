# E01 把另一张表改成程序认识的格式（选做）

别人给你的表里，编号可能叫 sample_id，你的程序里却叫 record_id。你要改列名、转换温度，让旧程序也能读这张新表。

先完成：P08；选做。本关主要练：csv.DictReader、字段改名、类型转换、记录来源。

第一次做题，先读 [怎么开始](../../START_HERE.md)。下面所有命令都在有 `check.py` 的 `python_handson_pack/` 目录运行。

## 要做成什么样

输入的一条记录如果 sample_id=A、label=demo、temperature=25、unit=C，输出对应的 record_id 应为 A、name 应为 demo、tg_value 应为 298.15、tg_unit 应为 K。
输入的文字 "true" 要转成 Python 的 True，不能直接用 bool("false") 判断真假。

## 打开哪里，按什么顺序写

先打开 `lessons/e01_import/task.py`。下面每一步都可以单独当作一次小练习；不要求一次写完整关。

1. **先看表头**：打开 data/provider_sample.csv，对照下方规则写出“原列名→新列名”。
2. **先转换一条，再转换多条**：在 adapt_rows 中建立新的结果字典。温度调用 P03，来源填调用者给的 source_name。
3. **连接 CSV 读取**：read_provider 用 DictReader 读表，再调用 adapt_rows。
4. **记录这份表的来历**：在 SOURCE_NOTES.md 标明当前使用的是教学样例；将来换真实资料时再写实际出处。

## 先检查一小步

这一关可跳过。先把本地样例转换好，不用去网上寻找材料数据库。

都写完后，再运行整关检查：

```powershell
py check.py E01
```

如果电脑使用 `python`，把命令里的 `py` 换成 `python`。这条命令会运行一组检查；只完成一小步时，其他检查失败是正常的。先看报错最后几行，只解决当前这个问题。

普通关卡不要改 `test_task.py`；它是已经准备好的检查程序。P06 的 `test_student.py` 则明确留给你填写。只定义函数后直接运行 task.py 可能没有输出，这不等于写错；使用本关检查命令或自己写调用。

## 遇到这些词怎么理解

“字段”就是字典里的项目名；“映射”在这里是列名一一对应；“可追溯”就是能查到数据从哪里来。

## 写完后核对的具体规则

这部分保留准确的函数名、返回格式和特殊情况，方便检查，也方便其他 AI 辅导。第一次不用全背下来；写到哪个函数，再对照哪条。

adapt_rows(rows, source_name) -> 标准字典列表。输入列 sample_id、label、temperature、unit、structure、is_synthetic；教学 CSV 的 is_synthetic 是字符串 true/false，不区分大小写；未知值抛 ValueError，不能默认为真实。
输出 record_id、name、smiles、tg_value（K浮点）、tg_unit='K'、is_synthetic（bool）、source（source_name）。不修改输入。不合法温度或空 ID 抛 ValueError，先不做隔离表。
read_provider(path, source_name) 用 csv.DictReader 并调用 adapt_rows。
实际转接真实数据时，source_name 不是来源证据的替代；本题只教转换，真实数据还需附原始出处、单位依据和许可。

## 完成以后再做

**基本完成**：函数按上述规则通过自动检查；需要展示或文件输出的部分，你也亲自看过结果。自动检查通过不代表后面的加练已经完成。

**再试着解释**：写清教学来源与真实来源的区别，不能因字段转换成功就认定数据科学有效。

**加练，主任务完成后再做**：增加一份不同列名的教学表，用配置字典指定列映射；实际真实数据由你后续选择，本包没有伪造实验来源。

加练写在 `variations.py`，自己补一个能核对结果的例子；原来的自动检查不一定检查加练。最后在 `NOTES.md` 写三句话：我写了什么、实际运行结果、哪里还不懂。

卡住时可以这样问 AI：“我在 E01 的第 __ 步，请先用日常语言解释这一步，再给一个不同输入的小例子。不要一次给我整关答案。”
