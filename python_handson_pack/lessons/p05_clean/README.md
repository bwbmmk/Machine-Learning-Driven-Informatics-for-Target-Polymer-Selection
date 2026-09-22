# P05 去掉错误和重复资料，再保存文件

上一关能找出问题，这一关要整理出能继续用的资料：坏的不要，重复的只留第一条，温度统一，并记下每条最后去了哪里。题目较长，可以分几次做。

先完成：P03、P04。本关主要练：复制字典、记录已出现的编号、调用前题、保存 JSON 和 CSV。

第一次做题，先读 [怎么开始](../../START_HERE.md)。下面所有命令都在有 `check.py` 的 `python_handson_pack/` 目录运行。

## 要做成什么样

输入 A（合法）、B（坏温度）、A（与第一条完全相同），应只保留第一条 A。
三条的处理结果依次是 `kept`（保留）、`invalid`（不合要求）、`duplicate`（完全重复）。
如果后一个 A 的内容不同，标记为 `duplicate_conflict`（编号一样，但内容不同），仍保留第一个合法 A。

原教学文件的目标是：12 条输入 → 6 条保留、5 条无效、1 条重复。

## 打开哪里，按什么顺序写

先打开 `lessons/p05_clean/task.py`。下面每一步都可以单独当作一次小练习；不要求一次写完整关。

1. **只做合法与错误的区分**：在 clean_records 中调用 P04 的检查。合法的字典先复制，再用 P03 算出 tg_k 放进复制品，不修改原字典。
2. **加上编号重复检查**：记住已经保留的编号及原始内容。后来遇到相同编号时，比较原始字典是否相同，再区分两种重复。
3. **给每条记结果**：每条输入都生成一条日志：原行号、编号、处理状态、原因。先让 clean_records 正确返回 cleaned 和 logs 两个列表。
4. **另一次练习再保存 JSON**：实现 save_bundle。先检查四个目标文件都不存在，再准备写入。写 cleaned.json（保留资料）和 summary.json（各类数量）。
5. **再保存两张 CSV 表**：cleaned.csv 是保留的资料，rejected.csv 是未保留资料的日志。空表也需要列名。完整列名和文件规则在下方核对表中。
6. **检查结果**：打开输出文件看内容，并确认 6+5+1+0=12。再次写同一目录应拒绝覆盖；需要再运行时换一个新目录。

## 先检查一小步

`clean_records` 的结果写作 `(cleaned, logs)`，表示一次交出两份结果，调用者可以用两个变量接住。先把它做对，再写 save_bundle，不用一次实现四个文件。

都写完后，再运行整关检查：

```powershell
py check.py P05
```

如果电脑使用 `python`，把命令里的 `py` 换成 `python`。这条命令会运行一组检查；只完成一小步时，其他检查失败是正常的。先看报错最后几行，只解决当前这个问题。

普通关卡不要改 `test_task.py`；它是已经准备好的检查程序。P06 的 `test_student.py` 则明确留给你填写。只定义函数后直接运行 task.py 可能没有输出，这不等于写错；使用本关检查命令或自己写调用。

## 遇到这些词怎么理解

“清洗”就是按规则整理资料；“日志”是每条的处理记录；“摘要”是数量汇总；CSV 是可用表格软件打开的文本表格。

## 写完后核对的具体规则

这部分保留准确的函数名、返回格式和特殊情况，方便检查，也方便其他 AI 辅导。第一次不用全背下来；写到哪个函数，再对照哪条。

clean_records(records) -> (cleaned, logs)。cleaned 保持输入顺序及全部原始字段，增加 tg_k。重复判断比较原始合法字典内容，不进行化学去重或单位等价去重。
每条日志恰含 row_number、record_id、status、reason；status 为 kept/invalid/duplicate/duplicate_conflict；kept 的 reason 为 ''，其他为非空说明。
save_bundle(cleaned, logs, output_dir) -> None，目录可自动创建。输出 cleaned.json、cleaned.csv、rejected.csv、summary.json。rejected 只包含非 kept 日志；CSV 用 UTF-8 和正确的 newline 处理，空表仍有表头。
summary 恰含 input_count、kept、invalid、duplicate、duplicate_conflict，均为整数。cleaned.csv 按实际记录字段并集导出；空列表使用 record_id,name,smiles,tg_value,tg_unit,is_synthetic,tg_k 表头。
四个目标文件任一个已存在就抛 FileExistsError，开始写之前检查全部目标；本关不要求防断电事务写入。
教学数据结果：6 kept、5 invalid、1 duplicate、0 conflict。

## 完成以后再做

**基本完成**：函数按上述规则通过自动检查；需要展示或文件输出的部分，你也亲自看过结果。自动检查通过不代表后面的加练已经完成。

**再试着解释**：手算一遍输入行数的去向；比较源文件的内容，确认未被覆盖。

**加练，主任务完成后再做**：自己添加同 ID 不同温度的记录，再添加包含新字段 source_note 的记录，确保都能解释和导出。

加练写在 `variations.py`，自己补一个能核对结果的例子；原来的自动检查不一定检查加练。最后在 `NOTES.md` 写三句话：我写了什么、实际运行结果、哪里还不懂。

卡住时可以这样问 AI：“我在 P05 的第 __ 步，请先用日常语言解释这一步，再给一个不同输入的小例子。不要一次给我整关答案。”
