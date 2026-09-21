# P05 清洗去重和保存

前置：P03、P04。知识：字典复制、去重、csv、json、文件保护。

## 你要亲手做的步骤

1. 先得到合法记录的复制品并新增 tg_k，不修改原始记录。
2. 按 ID 保留第一条合法记录，区分内容相同重复和内容冲突。
3. 为每条输入生成一条日志，核对数量守恒。
4. 写 save_bundle 导出四个文件；先检查已有文件再写，避免无意覆盖。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

clean_records(records) -> (cleaned, logs)。cleaned 保持输入顺序及全部原始字段，增加 tg_k。重复判断比较原始合法字典内容，不进行化学去重或单位等价去重。
每条日志恰含 row_number、record_id、status、reason；status 为 kept/invalid/duplicate/duplicate_conflict；kept 的 reason 为 ''，其他为非空说明。
save_bundle(cleaned, logs, output_dir) -> None，目录可自动创建。输出 cleaned.json、cleaned.csv、rejected.csv、summary.json。rejected 只包含非 kept 日志；CSV 用 UTF-8 和正确的 newline 处理，空表仍有表头。
summary 恰含 input_count、kept、invalid、duplicate、duplicate_conflict，均为整数。cleaned.csv 按实际记录字段并集导出；空列表使用 record_id,name,smiles,tg_value,tg_unit,is_synthetic,tg_k 表头。
四个目标文件任一个已存在就抛 FileExistsError，开始写之前检查全部目标；本关不要求防断电事务写入。
教学数据结果：6 kept、5 invalid、1 duplicate、0 conflict。

## 验收命令

在练习包根目录运行：

```powershell
py check.py P05
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

自己添加同 ID 不同温度的记录，再添加包含新字段 source_note 的记录，确保都能解释和导出。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

手算一遍输入行数的去向；比较源文件的内容，确认未被覆盖。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
