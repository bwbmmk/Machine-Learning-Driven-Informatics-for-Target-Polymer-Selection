# 分级提示

## 第 1 层
先处理空列表，再访问列；否则空 DataFrame 可能没有 tg_k 列。
## 第 2 层
查 to_numeric、loc 和 sort_values 的文档。相同值要保持顺序，选择稳定排序。
## 第 3 层
由 Pandas 得到的标量可能是 NumPy 类型；返回普通 Python 数字更方便写 JSON。

先返回 task.py 尝试，不必一次看完所有提示。
