# 共同规则与接口导航

每关README是直接执行标准；本包比早期总任务卡细化了返回值、输出文件名和P12需求。其他AI请以本包为准。

## 数据和代码

- 原始数据只读保留，变式放你自己的新文件。
- 名称、温度和结构字段均用于教学，不构成真实材料实验记录。
- 不把缺失、错误、未知和0混为一谈。
- 输入不变：除明确允许的保存函数外，处理函数不能改传入记录。
- P05去重按原始合法字典是否相同区分duplicate与duplicate_conflict。这是教学口径，不是科学数据库通用规则。
- record_id检查去空格后非空，但保留原字符串参与身份匹配；不要偷偷更改ID语义。
- 函数中不打印，除main等题目明确要求展示的入口。
- 不硬编码样本数量或ID去通过测试。测试会使用额外构造的输入，你也需要自己的变式。

## 日志和摘要

P04每行：row_number、record_id、ok、errors。
P05每行：row_number、record_id、status、reason；状态只有kept/invalid/duplicate/duplicate_conflict。
P05摘要：input_count、kept、invalid、duplicate、duplicate_conflict。
P09统计：count、min、max、mean；空输入后三项None。
P12摘要：input_count、kept、selected。

## 错误和保存

无效函数参数抛ValueError；文件不存在保留FileNotFoundError；拒绝覆盖用FileExistsError。
CLI把预期输入/文件错误转成stderr消息和退出2，不能吞掉未实现函数或代码缺陷。
保存前先检查本次所有目标文件，再开始写入。本包不要求实现跨文件事务或进程并发锁。

## 测试的范围

自动测试检查代表性的正常、错误与边界输入，不是完整形式化证明。
图的含义、代码是否易读、是否真的用Pandas/RF、是否独立完成，需要人工查看。
变式和P12新增的自由扩展，由你亲自补检查，不必为了凑数量写重复断言。
