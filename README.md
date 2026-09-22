I'm learning,maybe no useful things you want. 
# 用聚合物项目练习 Python

这个仓库记录一名信息安全专业学生的 Python 编程练习。Project 1 提供应用背景；当前重点是亲手写代码，逐步掌握文件处理、函数、调试、模块、命令行、数据分析和表达。

## 从这里开始

- **第一次做题先看 [怎么开始](python_handson_pack/START_HERE.md)**：具体打开哪个文件、第一步写什么、怎么运行和看报错。
- [完整练习包说明](python_handson_pack/README.md)：12 个主线关卡、4 个选做扩展。
- [下载 ZIP](releases/python_handson_pack.zip)：可独立解压使用；[SHA256 校验文件](releases/python_handson_pack.zip.sha256)。
- [学习路线](python_handson_pack/ROADMAP.md)与[学习进度](python_handson_pack/PROGRESS.md)。
- [AI 助教提示词](python_handson_pack/AI_TUTOR.md)：先提示，再审阅，让学习者亲手实现。
- [项目实施指南](项目实施指南/00_从这里开始.md)：总体规划及完整科研项目的备用参考。
- [原始项目要求](<references/Project 1(1).docx>)。

## 开始练习

克隆或下载仓库后，在仓库根目录打开终端：

```powershell
cd python_handson_pack
py check.py --list
py check.py P01
```

如果本机使用 `python` 命令，可以替换 `py`。打开 `lessons/p01_read/README.md`，然后亲手填写同目录的 `task.py`。前九关仅使用标准库，后期依赖见[环境说明](python_handson_pack/ENVIRONMENT.md)。

上面的 `py check.py P01` 会检查整关。第一次只写读取函数时，请用入门指南里的单项检查；没有写完的部分报错属于正常情况。

骨架未实现时出现 `NotImplementedError` 或测试失败是正常的；测试是待达成的目标。样例均为教学数据，不代表真实材料实验或模型效果。

## 目录约定

| 目录或文件 | 用途 |
|---|---|
| `python_handson_pack/` | 当前主线；题目、骨架、输入、测试、提示与个人记录 |
| `项目实施指南/` | 学习规划和后期科研参考 |
| `demo/` | 自己的小练习 |
| `references/` | 原始项目要求与 Git 工作流程图 |
| `releases/` | 可独立使用的 ZIP 快照与校验文件 |
| `archive/` | 早期第一题、散放题目和旧版上传副本，按来源归档 |
| `tools/` | 初始练习包生成脚本；开始写题后不要用它覆盖已有练习 |

日常只需打开 `python_handson_pack/`，在 `lessons/` 中写代码，在 `PROGRESS.md` 中记录进度。想写独立小实验时使用 `demo/`；查原题时使用 `references/`。

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
git add python_handson_pack 项目实施指南
git commit -m "Practice: describe the changes made"
git push
```

其他文件修改按实际路径补到 `git add`。Python 缓存、虚拟环境与生成的 `output/` 不提交；手写代码、题目笔记和进度可以提交。

ZIP 是当前提供的练习材料快照，后续修改源文件不会自动更新它；日常练习以仓库中的文件为准。无需每写一题都重新生成整个练习包。
