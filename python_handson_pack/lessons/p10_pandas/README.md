# P10 用 Pandas 对照实现

前置：P09；需 pandas。知识：DataFrame、数值类型、布尔筛选、结果核对。

## 你要亲手做的步骤

1. 按 ENVIRONMENT.md 建环境并安装 pandas，先检查解释器。
2. dataframe_report 接受字典列表，构造 DataFrame，显式把 tg_k 转成数值。
3. 给出区间筛选 ID、最高温前 n 的 ID，以及全表统计。
4. 用同一份数据调用 P09，对照所有结果。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

dataframe_report(records, low, high, n) -> {'filtered_ids':list,'top_ids':list,'stats':P09摘要}。
filtered 保留原顺序，top 稳定降序；统计针对全表，非筛选结果。支持 CSV 常见的数值字符串；空输入给空 ID 列表和空摘要。
low>high 或 n<0 抛 ValueError；不可解析/非有限 tg_k 抛 ValueError；不静默删行。
核心筛选和聚合应使用 Pandas，不能只转调 P09 以通过检查。

## 验收命令

在练习包根目录运行：

```powershell
py check.py P10
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

从你导出的 CSV 读入，加入空白单元格，说明错误处理与 fillna(0) 的差别。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

指出标准库版和 Pandas 版各自适合什么场景；自动验收不检查你是否实际用了 Pandas，需要自行/请 AI 审阅。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
