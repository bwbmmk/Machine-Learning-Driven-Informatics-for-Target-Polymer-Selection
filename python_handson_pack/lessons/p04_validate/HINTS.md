# 分级提示

## 第 1 层
validate_record 负责一条记录；check_records 负责循环和加行号。
## 第 2 层
把 ID 错误和温度错误分别追加到列表；温度错误只捕获 P03 约定的 ValueError。
## 第 3 层
enumerate 的 start 参数可以让行号从 1 开始；重复 ID 仍有不同原始行号。

先返回 task.py 尝试，不必一次看完所有提示。
