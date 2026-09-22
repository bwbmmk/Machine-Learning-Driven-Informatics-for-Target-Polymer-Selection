# 第一次做题：具体怎么开始

现在先做一个很小的程序：**打开一个资料文件，读出里面的记录，在屏幕上显示前几条。** 后面才慢慢加入查找、整理、保存和画图。你目前不需要先弄懂聚合物、化学结构或机器学习。

这里的资料都是编出来的练习数据。你可以把它想成一张物品清单：每件物品有编号、名字和一个温度数值。项目背景不会影响你先学会文件、列表、字典和函数。

## 先只打开三个文件

用你平时写 Python 的编辑器，打开整个 `python_handson_pack` 文件夹。暂时只看：

| 文件 | 你用它做什么 |
|---|---|
| [P01 题目](lessons/p01_read/README.md) | 看这一小步要达到什么结果 |
| [P01 的 task.py](lessons/p01_read/task.py) | 在这里亲手写代码 |
| [教学数据](data/teaching_records.json) | 看程序要读取的内容 |

`task.py` 是代码文件。`README.md` 是说明书。`test_task.py` 是已经写好的检查程序，第一题不用改它。`check.py` 帮你运行检查，也不用改。

项目外面的 `archive/` 是旧材料，`项目实施指南/` 是更完整的背景资料；开始这道题不需要同时打开它们。

## 把数据看成一张小表

文件最外面的 `[]` 表示多条资料组成的列表；里面每一对 `{}` 表示一条资料。读入 Python 后，一条资料就是一个字典。

| 文件里的名字 | 日常意思 | 第一题怎么用 |
|---|---|---|
| record_id | 编号，例如 EX01 | 显示出来 |
| name | 名字，例如 demo_alpha | 显示出来 |
| tg_value | 一个温度数值，例如 25 | 原样显示，不计算 |
| tg_unit | 温度单位，C 是摄氏度，K 是开尔文 | 原样显示 |
| smiles | 表示结构的文字 | 先跳过 |
| is_synthetic | 是否是人造样例 | 先跳过；本文件都是教学样例 |

JSON 是存这些资料的一种文本格式。JSON 里的 `true` 读入 Python 后是 `True`，`null` 读入后是 `None`。第一题用 `json.load` 读取，不需要自己处理这些替换。

## 第一次只完成“读文件”这一步

1. 打开 `lessons/p01_read/task.py`，找到 `def load_records(path):`。
2. `path` 表示调用者给你的文件地址。你要用这个地址打开文件，读出 JSON 内容，再交回结果。
3. 把这个函数里面的 `raise NotImplementedError(...)` 换成你写的代码。它的意思只是“这里还没写”，不能留在已经完成的函数末尾。
4. `def` 下面的代码需要缩进，通常是四个空格。函数名和括号里的参数名先保持原样，这样检查程序才能找到你的函数。
5. 按 Ctrl+S 保存。先不管 `preview_records` 和 `main`，它们还没写完是正常的。

需要学的东西很少：`open` 用来打开文件，`with` 帮你在用完后关闭它，`json.load` 把 JSON 文件读成 Python 对象，`return` 把结果交给调用者。具体用法可以边查边写；卡住就看 [P01 提示](lessons/p01_read/HINTS.md)。

### return 和 print 有什么区别

看一个与题目无关的小例子：

```python
def double(number):
    return number * 2

answer = double(4)
print(answer)
```

`return` 把 8 交给 answer，`print` 才把 8 显示出来。题目的读取函数也需要交回数据，让后面的程序能接着用；不能只显示内容却不返回。

## 终端到底怎么用

终端是输入运行命令的窗口。编辑器通常有“终端”菜单，也可以使用 PowerShell。下面命令输入终端，**不要写进 task.py，也不要写在 Python 的 `>>>` 后面**。如果你看到 `>>>`，先输入 `exit()` 回到终端。

这台电脑目前的练习目录是：

```powershell
cd "C:\Users\MR\Desktop\Machine Learning-Driven Informatics for Target Polymer Selection\python_handson_pack"
```

`cd` 是切换目录。看到当前目录末尾是 `python_handson_pack` 即可；已经在这里就不用重复切换。换电脑或移动文件夹后，使用实际地址。

先检查 Python 能否运行：

```powershell
py --version
```

如果提示找不到 `py`，试 `python --version`；哪个能运行，后面就一直用哪个替换命令开头的 `py`。不要为了开始第一题安装 Pandas、RDKit 或机器学习工具。

写好 load_records 后，**只检查这一小步**：

```powershell
py -m unittest lessons.p01_read.test_task.ReadTests.test_read_real_file -v
```

这串较长的命令先复制即可。它的意思是“运行 P01 中检查读取文件的那一项”。

- 最后出现 `OK`：这一项检查通过。第一小步完成，可以停下来休息。
- 出现 `NotImplementedError`：程序走到了还没填写的位置，或修改后忘了保存。
- 出现 `AssertionError`：程序给出的结果与检查要求不同。
- 出现 `SyntaxError` / `IndentationError`：先检查冒号、括号或缩进。
- 出现 `No module named lessons` / 找不到 `check.py`：先确认终端在上述练习目录。
- 整关检查最后出现 `AUTOMATED CHECKS PASSED`：自动检查通过；`NOT FINISHED` 表示还有检查未通过；`INCOMPLETE` 表示有检查被跳过，例如后期没安装所需的库，不能当作通关。

不用一次读懂全部报错。先看最后几行和提到的文件、行号；求助时把执行命令和完整报错一起发给 AI。

## 后面两小步什么时候写

读取成功后再做，顺序见 [P01 题目](lessons/p01_read/README.md)：

1. `preview_records`：从已有列表取出前 n 条，交回一个新列表。
2. `main`：调用前两个函数，用 print 显示总数和前三条。

这两步也可以分两次完成。都写好之后，在相同目录运行：

```powershell
py check.py P01
py -m lessons.p01_read.task
```

第一条检查整关的函数，第二条运行你的展示程序。第一条通过后，第二条仍需要你亲眼看结果：总数应为 12，前三个编号应是 EX01、EX02、EX03。未完成整关时，完整检查报错不是“你不适合做这个”，只是还差某一步。

## 一次练习做多少

一次只选一个小目标，例如“今天让 load_records 读出内容”。写几行、保存、运行、修一个问题即可，不要求一天做完一关。P05、P08、P12 工作多，分成几次做很正常。

先做 P01–P03：读文件、查资料、换算数字。做到这里后再看 P04。每关后面的“加练”和 E 开头的扩展可以以后再做；先完成主任务，也不等于已经完成加练。

把本次进度用一句话记在当前关的 `NOTES.md`，例如：“已写读取函数，单项检查 OK，尚未写预览函数。”不用写成正式报告。

## 可以直接发给其他 AI 的话

```text
我是 Python 初学者，正在做 P01 的“读取文件”这一步。
请先用简单中文说明：输入是什么、我要写什么、输出是什么。
再把这一步拆成最多三个小动作，不要一次讲后面的关卡。
遇到新词先解释；必要时用通讯录或成绩表举例。
我希望亲手写，请先给思路和一个小提示，不直接补完整题目。
我会贴当前 README、task.py 和运行结果，请按它们继续辅导。
```

如果连题目都不明白，直接说“先解释题意，不要写代码”。不需要先写出一份成熟方案才有资格求助。
