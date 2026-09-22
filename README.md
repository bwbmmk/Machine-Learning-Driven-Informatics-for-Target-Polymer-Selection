I'm learning,maybe no useful things you want. 
# 用聚合物项目练习 Python

这个仓库记录一名信息安全专业学生的 Python 编程练习。Project 1 提供应用背景；当前从基础语法开始，每次亲手写一个小程序，再逐步完成数据读取、整理和筛选。

## 从这里开始

- **当前主线：[新流程](新流程/README.md)**。14 个从空文件开始写的小程序；题目、自己的文件、可运行的对照示例分开放。
- [第一小题：打印项目名](新流程/任务卡/01_打印项目名.md)：今天只需写两行输出，运行成功后再做下一题。
- [新流程的进度记录](新流程/进度.md)：记录亲手写过和改进过的内容。

以下是之前准备的完整练习包和项目资料，供以后进阶或查阅；当前无需两套同时做。

- [旧版完整练习包的入门说明](python_handson_pack/START_HERE.md)：以后想做函数接口与自动检查题时再读。
- [完整练习包说明](python_handson_pack/README.md)：12 个主线关卡、4 个选做扩展。
- [下载 ZIP](releases/python_handson_pack.zip)：可独立解压使用；[SHA256 校验文件](releases/python_handson_pack.zip.sha256)。
- [学习路线](python_handson_pack/ROADMAP.md)与[学习进度](python_handson_pack/PROGRESS.md)。
- [AI 助教提示词](python_handson_pack/AI_TUTOR.md)：先提示，再审阅，让学习者亲手实现。
- [项目实施指南](项目实施指南/00_从这里开始.md)：总体规划及完整科研项目的备用参考。
- [原始项目要求](<references/Project 1(1).docx>)。

## 开始练习

克隆或下载仓库后，在仓库根目录打开终端，先做新流程第 01 题：

```powershell
cd 新流程
py 自己写/01_打印项目名.py
```

如果本机使用 `python` 命令，可以替换 `py`。先看 [第 01 题要求](新流程/任务卡/01_打印项目名.md)，在对应文件中从零写；写完并运行后，再查看同名的 `对照示例/`。这套新流程前 14 题只用 Python 自带功能。

旧的 `python_handson_pack/` 仍可用作后期补充，里面的骨架未实现时会报 `NotImplementedError`。新流程的 `自己写/` 则是注释占位的空程序，供你自己从第一行写起。样例均为教学数据，不代表真实材料实验或模型效果。

## 目录约定

| 目录或文件 | 用途 |
|---|---|
| `新流程/` | 当前主线；从零写的小程序、任务卡和对照示例 |
| `python_handson_pack/` | 先前的完整练习包，供后期进阶参考 |
| `项目实施指南/` | 学习规划和后期科研参考 |
| `demo/` | 自己的小练习 |
| `references/` | 原始项目要求与 Git 工作流程图 |
| `releases/` | 可独立使用的 ZIP 快照与校验文件 |
| `archive/` | 早期第一题、散放题目和旧版上传副本，按来源归档 |
| `tools/` | 初始练习包生成脚本；开始写题后不要用它覆盖已有练习 |

日常先打开 `新流程/`，在 `自己写/` 中写代码，在 `进度.md` 中记录进度。想写独立小实验时使用 `demo/`；查原题时使用 `references/`。

整理只移动材料并更新导航，没有合并或删除旧版练习。原目录去向见[归档说明](archive/README.md)。历史文件保留当时的说明和路径，当前执行方式以本页及完整练习包为准。

## 后续同步

在仓库根目录操作。开始修改前，如果工作区干净，可以先拉取：

```powershell
git pull --ff-only
```

写完一小步后查看差异，再提交推送：

```powershell
git status
git diff
git add 新流程 README.md
git commit -m "Practice: describe the changes made"
git push
```

其他文件修改按实际路径补到 `git add`。Python 缓存、虚拟环境与生成的 `output/` 不提交；手写代码、题目笔记和进度可以提交。

ZIP 是当前提供的练习材料快照，后续修改源文件不会自动更新它；日常练习以仓库中的文件为准。无需每写一题都重新生成整个练习包。
