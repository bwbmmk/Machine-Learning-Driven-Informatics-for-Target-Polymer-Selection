# P12 独立完成名字筛选小改版

前置：P08、P09；P10/P11可后补。知识：需求拆分、复用、集成、README。

## 你要亲手做的步骤

1. 本次固定需求：清洗后按名称关键词和 Tg 区间筛选，再取温度最高的前 N 条。
2. 先在 NOTES 写处理顺序、要复用哪些函数，再实现 select_records。
3. 实现 run_job，把清洗结果与选择结果一起导出，保留原清洗摘要。
4. 写新 CLI 和 MY_README.md，用另一份输入从头运行。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

select_records(records, keyword, low, high, n) -> 已清洗记录列表：先名称匹配，再闭区间，再稳定温度降序取前 n。空白关键词表示不过滤名称；非空匹配规则与 P02 相同。low>high/n<0 抛 ValueError。
run_job(input_path, output_dir, keyword, low, high, n) -> {'input_count':int,'kept':int,'selected':int}。
输出 P05 四文件，加 selected.json（列表）和 selection_summary.json（上述三字段）。任意六文件已存在即提前拒绝；参数无效或 JSON 根不是列表时，不创建输出目录。
CLI 参数 --input、--output-dir 必填；--keyword 默认空、--low/--high 必填 float、--top 默认10。成功 stdout 输出摘要 JSON；预期错误 stderr+退出2，成功0。
主数据取 keyword=demo、low=300、high=350、n=2，应选 EX11、EX10。
本包相较早期任务卡，将“任选改版”具体化为这一项，方便你不再临时等 AI 出题。

## 验收命令

在练习包根目录运行：

```powershell
py check.py P12
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

再独立加 --sort-by name 或温度最小值筛选中的一个功能，自己写测试和文档；这部分没有预先规定实现。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

让同学或新 AI 只看 MY_README.md 尝试运行；回看你是否能独立解释每个核心函数。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
