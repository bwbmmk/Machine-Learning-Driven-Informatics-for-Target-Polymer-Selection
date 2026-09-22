# E03 离线回归 API 练习

前置：P09；需 scikit-learn，选做。知识：X/y、训练测试、基线、误差。

## 你要亲手做的步骤

1. 使用包内 toy_regression.json，不需要下载真实数据。
2. 只取 x1、x2 为输入，target 为人为教学标签，ID 和标签不放入 X。
3. 固定 random_state=42，80/20 划分；仅在训练部分拟合 Dummy 和一个 RandomForestRegressor。
4. 算测试 RMSE，返回指标与划分 ID；不要反复挑种子。

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

train_and_evaluate(rows) -> {'baseline_rmse':float,'model_rmse':float,'n_train':int,'n_test':int,'train_ids':list,'test_ids':list}。
采用 train_test_split(test_size=0.2,random_state=42)。RandomForestRegressor 固定 n_estimators=50, random_state=42, n_jobs=1，其余默认。DummyRegressor 使用 mean。
不预设模型必须超过某个分数；训练数据需至少10行、ID唯一，x1/x2/target为有限数值，违约抛 ValueError。本关可不泛化其他类型。
全部数据是确定性生成的数值教学题，**不是聚合物结构或实验 Tg**。通过本关只说明掌握调用流程；将来用于材料时再采用真实结构特征、实验标签、分组划分与科学评估。

## 验收命令

在练习包根目录运行：

```powershell
py check.py E03
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

只在训练集内部再留一份验证集比较两种树深度，最终测试仍只用于报告；把额外选择写清楚。

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

代码审阅确认确实训练 RF、没有在测试集 fit；自动检查不能代替完整泄漏审计。

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
