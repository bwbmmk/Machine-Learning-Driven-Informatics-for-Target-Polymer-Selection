# P07 组合模块形成处理流程

前置：P01、P05、P06。知识：import、职责、调用链、无副作用。

## 你要亲手做的步骤

1. 本关已分出 io_utils.py、processing.py、task.py 三个职责文件。
2. io_utils 连接 P01 的读取与 P05 的保存；processing 连接 P05 清洗。
3. task.run_pipeline 依次调用读取、检查根对象、清洗、导出。
4. 画出调用顺序；不要复制前面已经正确的实现。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

io_utils.load_input(path) -> 原始 JSON 对象；io_utils.write_output(cleaned,logs,output_dir) -> None。
processing.process_records(records) -> (cleaned, logs)，可调用先前函数。
run_pipeline(input_path, output_dir) -> P05 定义的 summary 字典，同时生成四文件。JSON 根对象不是列表时抛 ValueError；文件/JSON/已有输出错误保留原异常。本题 import 模块不能自行读写文件。
这三个文件属于一个小包，包内可使用相对导入。所有运行从包根目录开始。

## 验收命令

在练习包根目录运行：

```powershell
py check.py P07
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

自己新建一个脚本，只调用 processing.process_records 处理内存中的三条记录，不进行文件读写。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

验收还需你阅读三个文件，确认职责分明；自动测试不能证明结构设计一定清晰。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
