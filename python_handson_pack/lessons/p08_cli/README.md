# P08 带预览功能的命令行工具

前置：P07。知识：argparse、退出状态、stderr、路径。

## 你要亲手做的步骤

1. 在 build_parser 中定义 --input、--output-dir、--preview，前两者必填。
2. main(argv=None) 解析参数并调用前面的模块。
3. 正常运行打印 JSON 摘要；--preview 只处理并打印，不创建输出目录。
4. 让用户输入错误与代码缺陷有不同处理：只捕获预期文件/数据异常。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

build_parser() -> ArgumentParser。main(argv=None) -> 0 成功或 2 预期错误。预期文件/JSON/根对象/输出已存在错误：stderr 非空且返回2；不要把 NotImplementedError 等编程缺陷吞掉。
成功时 stdout 是一个合法 JSON 摘要（允许缩进），不混其他文字。--help 使用 argparse 默认行为即可。
包根目录运行：py -m lessons.p08_cli.task --input data/teaching_records.json --output-dir output/run01
同一命令追加 --preview 时，output/run01 不应被创建或修改；仍需验证输入根对象。输出不能覆盖输入，沿用 P05 的拒绝覆盖规则。

## 验收命令

在练习包根目录运行：

```powershell
py check.py P08
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

添加 --limit-preview 参数，仅限制屏幕展示行数，不改变实际清洗结果；自己决定新的展示接口并记录。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

手动连续执行同一输出命令，确认第二次拒绝覆盖；读懂错误提示后换新输出目录。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
