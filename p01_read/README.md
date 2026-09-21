# P01 读入文件并预览

前置：无。知识：json、pathlib、列表字典、函数返回值。

## 你要亲手做的步骤

1. 打开 data/teaching_records.json，先描述外层与内层类型。
2. 在 load_records 中用上下文管理器读取 UTF-8 JSON，返回对象；本关不负责校验根对象类型。
3. 写 preview_records 返回前 n 条；不在这两个函数中打印。
4. 在 main 中读取默认教学文件，打印总条数和前三条的 ID、名称、原始数值及单位。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

- load_records(path) 接收字符串或 Path。JSON 解析或文件错误允许原样抛出。
- preview_records(records, n=3) 返回新列表，不改变输入；n 是整数，n<0 抛 ValueError；n=0 返回空列表。
- 原文件有 12 条，前 3 个 ID 是 EX01、EX02、EX03。另有 empty.json、malformed.json 供观察。
- main 的打印格式自由，内容由你手工验收。

## 验收命令

在练习包根目录运行：

```powershell
py check.py P01
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

增加只返回指定字段的预览函数，用不存在的字段测试你的约定。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

从包根目录用 py -m lessons.p01_read.task 运行展示；解释 Path(__file__) 为什么不依赖终端当前目录。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
