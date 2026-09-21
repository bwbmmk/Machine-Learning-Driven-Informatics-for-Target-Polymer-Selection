# 环境与命令

## 主线前九关

仅用 Python 标准库，代码写法兼容 Python 3.8 及以上；不需要 Jupyter、GPU、网络或 pip 包。优先沿用你已能运行脚本的解释器。完整包中的相对导入要求从包根目录运行命令，不能直接双击每个 task.py。

```powershell
py --version
py check.py --list
py check.py P03
py check.py P08 --through
```

--through 会从 P01 检查到指定关，早期未做完的题会失败；日常只查当前关即可。不同关复用已有实现，改公共函数后值得回查之前相关关卡。

## 到 P10 再建独立环境

先用 py -0p 查看已安装版本。可选择兼容相关库的64位 Python（例如3.11或3.12）；如果本机只有较旧版本，先完成标准库阶段，再为后续安装兼容版本，不必修改系统默认 Python。

以下示例假定你已安装3.11，命令都在包根目录执行：

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install pandas
.\.venv\Scripts\python.exe check.py P10
```

P11：

```powershell
.\.venv\Scripts\python.exe -m pip install matplotlib
.\.venv\Scripts\python.exe check.py P11
```

选做E02或E03时才分别安装：

```powershell
.\.venv\Scripts\python.exe -m pip install rdkit
.\.venv\Scripts\python.exe -m pip install scikit-learn
```

版本是否能安装以你当时的Python和官方安装说明为准；本包没有安装这些库或声称已经训练模型。运行成功后记录版本：

```powershell
.\.venv\Scripts\python.exe -m pip freeze > my-requirements.txt
```

若 py 不可用，使用 IDE 选定的解释器或 python。使用虚拟环境解释器路径，无需为激活脚本修改全局执行策略。

## P12 完成后的演示命令

这是你完成代码后的目标命令，现在骨架会报未实现：

```powershell
py -m lessons.p12_capstone.task --input data/teaching_records.json --output-dir output/final01 --keyword demo --low 300 --high 350 --top 2
```

预期选中EX11、EX10。已有输出会拒绝覆盖，换一个输出目录再运行。
