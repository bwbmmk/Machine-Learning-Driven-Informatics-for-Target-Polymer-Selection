# 打包检查记录

## 2026-09-22 易读说明更新

- 新增 START_HERE.md，把第一题拆为读取、预览、展示三小步。
- 改写 16 关的题意、例子和操作步骤；原有函数名、返回格式和特殊情况要求逐字保留。
- 70 个 Python 文件内容校验一致，没有改动学习者代码或测试。
- 本次涉及说明中的 45 个本地链接检查通过；P01 例子的记录数和编号已与输入文件核对。
- 实际运行 P01 的单项读取检查，成功找到该项测试；因读取函数仍为骨架，按预期报 NotImplementedError。没有声称学生已通过练习。
- 关卡清单命令已运行，显示 16 个易读标题。ZIP 从当前目录直接打包，不运行初版生成脚本。

## 初版材料检查记录

开发侧检查使用本机 Python 3.8.5。

- 70 个 Python 文件语法检查通过。
- 16 个关卡的题目、骨架、测试、提示、变式和笔记文件齐全。
- Markdown 本地链接、代码块和文本控制字符检查通过。
- 清洗数量、重复和筛选预期值经过独立核对。
- --list 与非法参数退出状态已实际验证。
- 逐个启动全部16个关卡验收，共加载 50 个测试；未完成骨架按预期失败，可选依赖缺失按未完成处理。没有把骨架验收标为学习者通过。
- 未安装可选依赖；未完成学习者的实现，也没有声称所有目标程序已通过功能验收。

|关卡|加载测试数|骨架状态|
|---|---|---|
|P01|4|expected unfinished|
|P02|3|expected unfinished|
|P03|3|expected unfinished|
|P04|3|expected unfinished|
|P05|4|expected unfinished|
|P06|6|expected unfinished|
|P07|3|expected unfinished|
|P08|3|expected unfinished|
|P09|3|expected unfinished|
|P10|2|dependency skipped|
|P11|2|dependency skipped|
|P12|4|expected unfinished|
|E01|3|expected unfinished|
|E02|3|dependency skipped|
|E03|2|dependency skipped|
|E04|2|expected unfinished|
