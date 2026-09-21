# P09 筛选排序与摘要

前置：P05；建议完成 P08。知识：sorted、statistics、空结果、参数校验。

## 你要亲手做的步骤

1. 对清洗记录写闭区间筛选。
2. 写不改变输入的 top_n，最高温度优先，相同温度保持原顺序。
3. 对所有输入记录统计数量、最小值、最大值、平均数。
4. 写 demo 调用 P05 的清洗结果，不手工录入正式输入。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

filter_range(records, low, high) -> 列表，包含 low<=tg_k<=high；low>high 抛 ValueError。
top_n(records,n) -> 最高温前 n 条；n 为整数，负数抛 ValueError，0 返回 []。
summarize(records) -> {'count':int,'min':float或None,'max':float或None,'mean':float或None}。
三个函数不改变输入。已清洗数据的 tg_k 假定为有限数值。
6 条清洗数据中，300–350 K 筛得 EX02、EX10、EX11；此为规则筛选，不是预测。

## 验收命令

在练习包根目录运行：

```powershell
py check.py P09
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

新增 median 字段并写手算检查；不要改原 summarize 的接口，另写 summarize_extended。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

拿纸算 [300,350,350,400] 的结果，解释为什么 count 和筛选后 count 不是同一统计口径。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
