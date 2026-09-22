# P01 打开数据文件，显示前几条记录

你有一个装着 12 条资料的文件。写程序把它读进来，然后看看前 3 条。这和读取通讯录、商品清单是同一类练习。

先完成：无。本关主要练：打开文件；用 json.load 读取；用 return 交出结果；从列表取前几项。

第一次做题，先读 [怎么开始](../../START_HERE.md)。下面所有命令都在有 `check.py` 的 `python_handson_pack/` 目录运行。

## 要做成什么样

文件中一条资料长这样（先只看这几个字段）：

```json
{"record_id": "EX01", "name": "demo_alpha", "tg_value": 25, "tg_unit": "C"}
```

把它理解成“编号 EX01，名字 demo_alpha，温度 25 摄氏度”。`record_id` 就是编号，`name` 是名字；目前不必研究名字代表什么材料。

你最后的屏幕输出可以是：

```text
记录总数：12
EX01 demo_alpha 25 C
EX02 demo_beta 310 K
EX03 demo_gamma -20  c
```

排版自由。EX03 的原始单位两边有空格，数值也是字符串；本题照原样读取，后面再处理。不能直接把这些结果写死在程序中。

## 打开哪里，按什么顺序写

先打开 `lessons/p01_read/task.py`。下面每一步都可以单独当作一次小练习；不要求一次写完整关。

1. **只看懂一条资料**：打开 `data/teaching_records.json`。最外面的 `[]` 表示一组记录，每对 `{}` 是一条记录。找到 EX01 的名字和温度即可；先跳过 `smiles`。
2. **只写 load_records(path)**：打开本关 `task.py`。`path` 是文件地址；函数要打开这个文件，用 `json.load` 读出内容，再 `return` 交给调用者。把函数里的 `raise NotImplementedError(...)` 换成自己的代码。先不改另外两个函数。
3. **检查刚写的读取函数**：在练习包目录运行下面“只查第一小步”的命令。如果看到 `OK`，说明这个例子的文件读取通过了；还不代表整关完成。
4. **再写 preview_records(records, n=3)**：`records` 是读出来的列表；`n` 是想看几条，没填时按 3 条。返回前 n 条组成的新列表。先处理普通情况，再补 n=0、n 比记录多、n<0 三种情况。n<0 时用 `raise ValueError(...)` 表示参数不合要求。
5. **最后写 main()**：`DATA_PATH` 已经指向教学文件，先直接使用。依次调用读取函数、预览函数，用 `print` 显示总数和每条记录的四个字段。只有这一部分负责屏幕展示。
6. **做完整检查并展示**：运行 `py check.py P01`，然后运行 `py -m lessons.p01_read.task`。前者检查函数结果，后者运行 main 让你看到实际展示。

## 先检查一小步

只查第一小步，在有 `check.py` 的目录运行：

```powershell
py -m unittest lessons.p01_read.test_task.ReadTests.test_read_real_file -v
```

继续检查“能否读另一个文件”，防止只适用于默认文件：

```powershell
py -m unittest lessons.p01_read.test_task.ReadTests.test_arbitrary_file -v
```

`preview_records([10, 20, 30], 2)` 应交出 `[10, 20]`；`preview_records([10, 20], 0)` 应交出 `[]`。这些是手算例子，不是完整答案。

都写完后，再运行整关检查：

```powershell
py check.py P01
```

如果电脑使用 `python`，把命令里的 `py` 换成 `python`。这条命令会运行一组检查；只完成一小步时，其他检查失败是正常的。先看报错最后几行，只解决当前这个问题。

普通关卡不要改 `test_task.py`；它是已经准备好的检查程序。P06 的 `test_student.py` 则明确留给你填写。只定义函数后直接运行 task.py 可能没有输出，这不等于写错；使用本关检查命令或自己写调用。

## 遇到这些词怎么理解

`return`：把结果交回调用它的地方。`print`：只负责显示。`Path`：表示文件地址的工具。现在直接用已有的 DATA_PATH，读懂它的写法可以放到完成本题以后。

## 写完后核对的具体规则

这部分保留准确的函数名、返回格式和特殊情况，方便检查，也方便其他 AI 辅导。第一次不用全背下来；写到哪个函数，再对照哪条。

- load_records(path) 接收字符串或 Path。JSON 解析或文件错误允许原样抛出。
- preview_records(records, n=3) 返回新列表，不改变输入；n 是整数，n<0 抛 ValueError；n=0 返回空列表。
- 原文件有 12 条，前 3 个 ID 是 EX01、EX02、EX03。另有 empty.json、malformed.json 供观察。
- main 的打印格式自由，内容由你手工验收。

## 完成以后再做

**基本完成**：函数按上述规则通过自动检查；需要展示或文件输出的部分，你也亲自看过结果。自动检查通过不代表后面的加练已经完成。

**再试着解释**：从包根目录用 py -m lessons.p01_read.task 运行展示；解释 Path(__file__) 为什么不依赖终端当前目录。

**加练，主任务完成后再做**：增加只返回指定字段的预览函数，用不存在的字段测试你的约定。

加练写在 `variations.py`，自己补一个能核对结果的例子；原来的自动检查不一定检查加练。最后在 `NOTES.md` 写三句话：我写了什么、实际运行结果、哪里还不懂。

卡住时可以这样问 AI：“我在 P01 的第 __ 步，请先用日常语言解释这一步，再给一个不同输入的小例子。不要一次给我整关答案。”
