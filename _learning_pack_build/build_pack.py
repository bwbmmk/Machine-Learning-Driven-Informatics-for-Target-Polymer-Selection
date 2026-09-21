"""Build an independent exercise pack. This script does not contain task solutions."""
from pathlib import Path
import json
import textwrap
import zipfile

WORKSPACE = Path(__file__).resolve().parent.parent
ROOT = WORKSPACE / 'python_handson_pack'
LESSONS = []


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + '\n', encoding='utf-8')


def lesson(code, slug, title, deps, skills, steps, contract, starter, tests, hints, variation, manual, imports=''):
    folder = 'lessons/' + slug
    LESSONS.append(dict(id=code, folder=folder, title=title, dependencies=deps))
    write(folder + '/__init__.py', '')
    write(folder + '/task.py', starter)
    write(folder + '/test_task.py', '''
import copy
import json
import math
from pathlib import Path
import tempfile
import unittest
from lessons.%s import task
from support import DATA, read_fixture
%s

%s
''' % (slug, imports, textwrap.dedent(tests).strip()))
    write(folder + '/README.md', '''
# %s %s

前置：%s。知识：%s。

## 你要亲手做的步骤

%s

每次只完成一步并运行一次。卡住超过约 20 分钟时再读 HINTS.md 的第一层。

## 函数和行为约定

%s

## 验收命令

在练习包根目录运行：

```powershell
py check.py %s
```

先前关卡有未完成的依赖时，先完成它们。未填写的骨架报 NotImplementedError 是预期行为。
测试不要求完全一致的错误文字，除非本题规定了机器读取的状态码。不要改测试去迎合错误程序。

## 独立变式

%s

变式写到 variations.py，可复用本关函数。提供的自动测试不覆盖所有变式，自己增加一个验证例子。

## 人工检查与表达

%s

结束后在 NOTES.md 记录你运行过的命令、一个错误原因和仍不理解的地方。
''' % (code, title, deps, skills, steps, contract, code, variation, manual))
    write(folder + '/HINTS.md', '# 分级提示\n\n' + hints + '\n\n先返回 task.py 尝试，不必一次看完所有提示。')
    write(folder + '/NOTES.md', '# 我的练习记录\n\n- 日期：\n- 我写的函数：\n- 运行命令与结果：\n- 一个错误及原因：\n- 独立变式：\n- 我仍需提示的部分：\n')
    write(folder + '/variations.py', '"""本关独立变式，由你选择或按 README 要求完成。"""\n')


write('lessons/__init__.py', '')
write('support.py', '''
"""已提供的练习基础设施：定位测试数据，不实现任何学习任务。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'

def read_fixture(name='teaching_records.json'):
    with (DATA / name).open(encoding='utf-8') as stream:
        return json.load(stream)
''')

lesson('P01', 'p01_read', '读入文件并预览', '无', 'json、pathlib、列表字典、函数返回值',
'''1. 打开 data/teaching_records.json，先描述外层与内层类型。
2. 在 load_records 中用上下文管理器读取 UTF-8 JSON，返回对象；本关不负责校验根对象类型。
3. 写 preview_records 返回前 n 条；不在这两个函数中打印。
4. 在 main 中读取默认教学文件，打印总条数和前三条的 ID、名称、原始数值及单位。''',
'''- load_records(path) 接收字符串或 Path。JSON 解析或文件错误允许原样抛出。
- preview_records(records, n=3) 返回新列表，不改变输入；n 是整数，n<0 抛 ValueError；n=0 返回空列表。
- 原文件有 12 条，前 3 个 ID 是 EX01、EX02、EX03。另有 empty.json、malformed.json 供观察。
- main 的打印格式自由，内容由你手工验收。''',
'''
"""P01：你负责读取和预览逻辑。"""
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / 'data' / 'teaching_records.json'

def load_records(path):
    raise NotImplementedError('TODO: 读取 JSON')

def preview_records(records, n=3):
    raise NotImplementedError('TODO: 返回前 n 条')

def main():
    raise NotImplementedError('TODO: 调用上述函数并打印结果')

if __name__ == '__main__':
    main()
''',
'''
class ReadTests(unittest.TestCase):
    def test_read_real_file(self):
        rows = task.load_records(DATA / 'teaching_records.json')
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows[0]['record_id'], 'EX01')
    def test_arbitrary_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'other.json'
            p.write_text('[{"record_id": "新输入"}]', encoding='utf-8')
            self.assertEqual(task.load_records(str(p)), [{'record_id': '新输入'}])
    def test_preview_boundaries(self):
        rows = [{'a': 1}, {'a': 2}]
        before = copy.deepcopy(rows)
        self.assertEqual(task.preview_records(rows, 1), rows[:1])
        self.assertEqual(task.preview_records(rows, 0), [])
        self.assertEqual(task.preview_records(rows, 99), rows)
        self.assertEqual(rows, before)
        with self.assertRaises(ValueError):
            task.preview_records(rows, -1)
    def test_empty_and_bad_json(self):
        self.assertEqual(task.load_records(DATA / 'empty.json'), [])
        with self.assertRaises(json.JSONDecodeError):
            task.load_records(DATA / 'malformed.json')
''',
'''## 第 1 层
读取是文件到 Python 对象，打印只是展示。先写能 return 的函数。
## 第 2 层
查 json.load 与 json.loads 的参数区别；用 with 管理文件。
## 第 3 层
列表切片可以处理 n 大于长度的情况；但负 n 需要先按题意拒绝。''',
'增加只返回指定字段的预览函数，用不存在的字段测试你的约定。',
'从包根目录用 py -m lessons.p01_read.task 运行展示；解释 Path(__file__) 为什么不依赖终端当前目录。')

lesson('P02', 'p02_query', '查询与重复记录', 'P01', '遍历、匹配、字符串、空结果',
'''1. 写 find_by_id，注意 ID 可能重复。
2. 写 search_by_name，处理空白关键词和缺 name 的记录。
3. 用 EX02 验证重复项，用不存在的 ID 验证空结果。
4. 从 P01 读取真实教学列表再调用查询函数。''',
'''输入 records 为字典列表。find_by_id 做原始 ID 精确匹配，返回全部命中，顺序与输入一致。
search_by_name 对关键词去空格，使用不区分大小写的子串匹配；空关键词返回 []。
name 缺失、null 或非字符串时当作不可匹配。两个函数都不改变输入。''',
'''
def find_by_id(records, record_id):
    raise NotImplementedError('TODO: 返回全部匹配项')

def search_by_name(records, keyword):
    raise NotImplementedError('TODO: 名称子串匹配')
''',
'''
class QueryTests(unittest.TestCase):
    def test_duplicate_and_missing(self):
        rows = read_fixture()
        self.assertEqual(len(task.find_by_id(rows, 'EX02')), 2)
        self.assertEqual(task.find_by_id(rows, 'absent'), [])
    def test_new_input_order_and_no_mutation(self):
        rows = [{'record_id': 'q', 'v': 2}, {'record_id': 'z'}, {'record_id': 'q', 'v': 1}]
        old = copy.deepcopy(rows)
        self.assertEqual(task.find_by_id(rows, 'q'), [rows[0], rows[2]])
        self.assertEqual(rows, old)
    def test_names(self):
        rows = [{'name': 'Alpha_X'}, {}, {'name': None}, {'name': 8}, {'name': 'xALPHA'}]
        self.assertEqual(task.search_by_name(rows, ' alpha '), [rows[0], rows[4]])
        self.assertEqual(task.search_by_name(rows, '  '), [])
        self.assertEqual(task.search_by_name([], 'a'), [])
''',
'''## 第 1 层
先创建结果列表；命中后添加，不要在第一次命中时结束整个函数。
## 第 2 层
用 get 取可能不存在的字段；对字符串做 strip 与 casefold。
## 第 3 层
返回值永远是列表，哪怕零条或一条。这样调用者更容易处理。''',
'自己构造 5 条输入，再建立 ID 到记录列表的索引，比较重复查询与一次建索引的思路。',
'解释为什么字典直接映射 ID 到单条记录可能丢失信息。')

lesson('P03', 'p03_units', '温度转换与边界', 'P01', '函数契约、float、math.isfinite、ValueError',
'''1. 先实现合法数值 C/K 到 K 的转换。
2. 添加字符串数值、单位空格和大小写处理。
3. 拒绝布尔值、空白、null、非有限数和未知单位。
4. 添加反向转换并手算几个结果。''',
'''to_kelvin(value, unit) 接受 int/float 或数值字符串（bool 除外），unit 必须为字符串 C/K，忽略两端空格和大小写。返回 float；结果必须 >0 且有限；不满足约定一律 ValueError。
kelvin_to_celsius(value) 使用相同的数值检查，要求输入 K>0。
25 C=298.15 K；-20 C=253.15 K；0 C 合法而 0 K 不接受。题目采用严格 >0 的教学规则。''',
'''
import math

def to_kelvin(value, unit):
    raise NotImplementedError('TODO: 输入检查和转换')

def kelvin_to_celsius(value):
    raise NotImplementedError('TODO: 反向转换')
''',
'''
class UnitTests(unittest.TestCase):
    def test_valid(self):
        for value, unit, expected in [(25,'C',298.15),('-20',' c ',253.15),(310,'K',310.0),(0,'C',273.15)]:
            with self.subTest(value=value, unit=unit):
                result = task.to_kelvin(value, unit)
                self.assertIsInstance(result, float)
                self.assertAlmostEqual(result, expected)
    def test_invalid(self):
        pairs = [(None,'C'),(True,'C'),('', 'C'),('warm','C'),('nan','K'),('inf','K'),(0,'K'),(-300,'C'),(5,'F'),(5,None),([], 'K')]
        for value, unit in pairs:
            with self.subTest(value=value, unit=unit):
                with self.assertRaises(ValueError):
                    task.to_kelvin(value, unit)
    def test_roundtrip(self):
        for c in [-100.0, 0.0, 37.5, 500.0]:
            self.assertAlmostEqual(task.kelvin_to_celsius(task.to_kelvin(c,'C')), c)
        with self.assertRaises(ValueError):
            task.kelvin_to_celsius(0)
''',
'''## 第 1 层
顺序可以是类型检查、解析数值、检查有限性、识别单位、检查转换结果。
## 第 2 层
bool 在 Python 中和 int 有继承关系，要单独考虑。float('nan') 不会抛转换错误。
## 第 3 层
只在你预期发生类型/数值转换错误的位置捕获异常，转换成有意义的 ValueError。''',
'新增两个断言：一个贴近绝对零度但仍合法的值，一个刚低于界限的值。',
'不用查答案，解释“能转成 float”和“是可接受的温度”为什么是两件事。')

lesson('P04', 'p04_validate', '批量校验与逐行报告', 'P03', '函数组合、错误列表、enumerate',
'''1. 写单行校验，先处理根对象不是字典。
2. 检查 record_id 和温度，不因第一个字段失败漏掉另一个字段问题。
3. 批量生成带原始行号的报告；每行只占一个报告元素。
4. 解释 12 条教学数据中哪 5 条不通过。''',
'''validate_record(row) 返回错误字符串列表，合法时 []。非字典只需一条说明；ID 必须是去空格后非空的字符串，校验不改原 ID。温度规则复用 P03。
check_records(records) 返回列表，每项恰含 row_number（从1起）、record_id（非字典或没有字段时为 None）、ok（bool）、errors（字符串列表）。name/smiles 此时不校验。允许收集多条原因，不要求错误原文完全一致。''',
'''
from lessons.p03_units.task import to_kelvin

def validate_record(row):
    raise NotImplementedError('TODO: 返回所有检查原因')

def check_records(records):
    raise NotImplementedError('TODO: 逐行报告')
''',
'''
class ValidateTests(unittest.TestCase):
    def test_fixture_counts(self):
        report = task.check_records(read_fixture())
        self.assertEqual(len(report), 12)
        self.assertEqual(sum(r['ok'] for r in report), 7)
        self.assertEqual([r['record_id'] for r in report if not r['ok']], ['EX04','EX05','EX06','EX07','EX08'])
        self.assertEqual([r['row_number'] for r in report], list(range(1,13)))
    def test_multi_error_and_shape(self):
        self.assertGreaterEqual(len(task.validate_record({'tg_value': 'bad', 'tg_unit': 'K'})), 2)
        self.assertTrue(task.validate_record(None))
        self.assertEqual(task.check_records([]), [])
        r = task.check_records([None])[0]
        self.assertEqual(set(r), {'row_number','record_id','ok','errors'})
        self.assertIsNone(r['record_id'])
        self.assertIs(r['ok'], False)
        self.assertTrue(all(isinstance(x, str) and x for x in r['errors']))
    def test_optional_fields_and_no_mutation(self):
        row = {'record_id':'new', 'tg_value':20, 'tg_unit':'C', 'smiles':'bad'}
        old = copy.deepcopy(row)
        self.assertEqual(task.validate_record(row), [])
        self.assertEqual(row, old)
''',
'''## 第 1 层
validate_record 负责一条记录；check_records 负责循环和加行号。
## 第 2 层
把 ID 错误和温度错误分别追加到列表；温度错误只捕获 P03 约定的 ValueError。
## 第 3 层
enumerate 的 start 参数可以让行号从 1 开始；重复 ID 仍有不同原始行号。''',
'加一个不影响有效性的 warning 列，提示缺少 name，先写清 warning 和 error 的区别。',
'能够说明 EX09 的通过仅指温度/ID 校验通过，绝不代表结构合法。')

lesson('P05', 'p05_clean', '清洗去重和保存', 'P03、P04', '字典复制、去重、csv、json、文件保护',
'''1. 先得到合法记录的复制品并新增 tg_k，不修改原始记录。
2. 按 ID 保留第一条合法记录，区分内容相同重复和内容冲突。
3. 为每条输入生成一条日志，核对数量守恒。
4. 写 save_bundle 导出四个文件；先检查已有文件再写，避免无意覆盖。''',
'''clean_records(records) -> (cleaned, logs)。cleaned 保持输入顺序及全部原始字段，增加 tg_k。重复判断比较原始合法字典内容，不进行化学去重或单位等价去重。
每条日志恰含 row_number、record_id、status、reason；status 为 kept/invalid/duplicate/duplicate_conflict；kept 的 reason 为 ''，其他为非空说明。
save_bundle(cleaned, logs, output_dir) -> None，目录可自动创建。输出 cleaned.json、cleaned.csv、rejected.csv、summary.json。rejected 只包含非 kept 日志；CSV 用 UTF-8 和正确的 newline 处理，空表仍有表头。
summary 恰含 input_count、kept、invalid、duplicate、duplicate_conflict，均为整数。cleaned.csv 按实际记录字段并集导出；空列表使用 record_id,name,smiles,tg_value,tg_unit,is_synthetic,tg_k 表头。
四个目标文件任一个已存在就抛 FileExistsError，开始写之前检查全部目标；本关不要求防断电事务写入。
教学数据结果：6 kept、5 invalid、1 duplicate、0 conflict。''',
'''
import csv
import json
from pathlib import Path
from lessons.p03_units.task import to_kelvin
from lessons.p04_validate.task import validate_record

def clean_records(records):
    raise NotImplementedError('TODO: 清洗并返回全部行日志')

def save_bundle(cleaned, logs, output_dir):
    raise NotImplementedError('TODO: 导出四个文件，保护已有输出')
''',
'''
import csv

class CleanTests(unittest.TestCase):
    def test_fixture(self):
        rows = read_fixture()
        old = copy.deepcopy(rows)
        clean, logs = task.clean_records(rows)
        self.assertEqual([r['record_id'] for r in clean], ['EX01','EX02','EX03','EX09','EX10','EX11'])
        self.assertEqual(rows, old)
        self.assertEqual(len(logs), 12)
        self.assertEqual(sum(r['status']=='invalid' for r in logs), 5)
        self.assertEqual(logs[10]['status'], 'duplicate')
        self.assertAlmostEqual(clean[0]['tg_k'], 298.15)
        self.assertTrue(all(r['is_synthetic'] for r in clean))
    def test_conflict_and_invalid_first(self):
        a = {'record_id':'x', 'tg_value':20, 'tg_unit':'C'}
        bad = dict(a, tg_value='bad')
        other = dict(a, tg_value=30)
        clean, logs = task.clean_records([bad, a, dict(a), other])
        self.assertEqual([r['status'] for r in logs], ['invalid','kept','duplicate','duplicate_conflict'])
        self.assertEqual(len(clean), 1)
        for row in logs:
            self.assertEqual(set(row), {'row_number','record_id','status','reason'})
            if row['status'] != 'kept': self.assertTrue(row['reason'])
    def test_export_and_no_overwrite(self):
        clean, logs = task.clean_records(read_fixture())
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'new'
            task.save_bundle(clean, logs, out)
            self.assertEqual(json.loads((out/'cleaned.json').read_text(encoding='utf-8')), clean)
            summary = json.loads((out/'summary.json').read_text(encoding='utf-8'))
            self.assertEqual(summary, dict(input_count=12, kept=6, invalid=5, duplicate=1, duplicate_conflict=0))
            with (out/'cleaned.csv').open(encoding='utf-8-sig', newline='') as f:
                self.assertEqual(len(list(csv.DictReader(f))), 6)
            with (out/'rejected.csv').open(encoding='utf-8-sig', newline='') as f:
                self.assertEqual(len(list(csv.DictReader(f))), 6)
            before = {p.name:p.read_bytes() for p in out.iterdir()}
            with self.assertRaises(FileExistsError): task.save_bundle(clean, logs, out)
            self.assertEqual(before, {p.name:p.read_bytes() for p in out.iterdir()})
    def test_empty_export(self):
        self.assertEqual(task.clean_records([]), ([], []))
        with tempfile.TemporaryDirectory() as tmp:
            task.save_bundle([], [], tmp)
            with (Path(tmp)/'cleaned.csv').open(encoding='utf-8-sig', newline='') as f:
                reader = csv.DictReader(f)
                self.assertIn('tg_k', reader.fieldnames)
                self.assertEqual(list(reader), [])
''',
'''## 第 1 层
先清洗，再保存；用字典维护已经保留过的 ID 及其原始内容。
## 第 2 层
校验失败的首条记录不应占用 ID。复制 row 后增加 tg_k；别直接改 row。
## 第 3 层
先创建所有输出路径清单并检查是否已存在，再逐个写。汇总可以从日志状态计数。''',
'自己添加同 ID 不同温度的记录，再添加包含新字段 source_note 的记录，确保都能解释和导出。',
'手算一遍输入行数的去向；比较源文件的内容，确认未被覆盖。')

lesson('P06', 'p06_debug', '修复三个缺陷并自己写测试', 'P05', '最小复现、unittest、traceback、回归',
'''1. task.py 中有三个故意写错的函数，先预测它们在哪些输入下失败。
2. 在 test_student.py 先写出会失败的测试，再修改 task.py。
3. 每修一处就运行自己的测试和本包测试。
4. 记录输入、原因、修复和如何防止再次出错。''',
'''c_to_k(value) 本题只处理有限数值且 value>-273.15，不要求重复实现 P03 全部校验。
find_all(records, key) 必须返回所有 record_id==key 的记录列表，保留顺序。
mean_or_none(values) 空列表返回 None，否则返回算术平均数。
test_student.py 三个测试必须由你亲手补完；验收命令会同时运行它们。''',
'''
"""下面是故意有缺陷的程序。先写测试重现，再修复。"""

def c_to_k(value):
    return value + 273  # BUG: 请用手算例子定位

def find_all(records, key):
    for row in records:
        if row['record_id'] == key:
            return row  # BUG: 返回值与重复情况
    return None

def mean_or_none(values):
    return sum(values) / len(values)  # BUG: 边界输入
''',
'''
class DebugTests(unittest.TestCase):
    def test_offset(self):
        self.assertAlmostEqual(task.c_to_k(12), 285.15)
    def test_duplicates(self):
        rows = [{'record_id':'a'},{'record_id':'b'},{'record_id':'a'}]
        self.assertEqual(task.find_all(rows,'a'), [rows[0],rows[2]])
        self.assertEqual(task.find_all(rows,'x'), [])
    def test_empty_mean(self):
        self.assertIsNone(task.mean_or_none([]))
        self.assertEqual(task.mean_or_none([2,4,9]), 5)
''',
'''## 第 1 层
挑一个可手算的输入，不用 1000 条数据重现错误。
## 第 2 层
返回第一条记录与返回记录列表是接口层面的差异。
## 第 3 层
空列表平均数没有可用结果，题目约定用 None；不要伪造为 0。''',
'独立增加一条测试，使它能抓住“去掉重复记录”这种错误修复。',
'不要仅把测试断言改成程序现有结果；说明测试为什么代表题目要求。')
write('lessons/p06_debug/test_student.py', '''
"""请亲手编写这三个测试。写完后删除各自的 NotImplementedError。"""
import unittest
from lessons.p06_debug import task

class MyRegressionTests(unittest.TestCase):
    def test_temperature(self):
        raise NotImplementedError('TODO: 选一个与验收测试不同的手算值')

    def test_duplicate_id(self):
        raise NotImplementedError('TODO: 构造重复 ID 并断言全部保留')

    def test_empty_mean(self):
        raise NotImplementedError('TODO: 明确空输入的行为')
''')

lesson('P07', 'p07_modules', '组合模块形成处理流程', 'P01、P05、P06', 'import、职责、调用链、无副作用',
'''1. 本关已分出 io_utils.py、processing.py、task.py 三个职责文件。
2. io_utils 连接 P01 的读取与 P05 的保存；processing 连接 P05 清洗。
3. task.run_pipeline 依次调用读取、检查根对象、清洗、导出。
4. 画出调用顺序；不要复制前面已经正确的实现。''',
'''io_utils.load_input(path) -> 原始 JSON 对象；io_utils.write_output(cleaned,logs,output_dir) -> None。
processing.process_records(records) -> (cleaned, logs)，可调用先前函数。
run_pipeline(input_path, output_dir) -> P05 定义的 summary 字典，同时生成四文件。JSON 根对象不是列表时抛 ValueError；文件/JSON/已有输出错误保留原异常。本题 import 模块不能自行读写文件。
这三个文件属于一个小包，包内可使用相对导入。所有运行从包根目录开始。''',
'''
from . import io_utils, processing

def run_pipeline(input_path, output_dir):
    raise NotImplementedError('TODO: 组合流程并返回 summary')
''',
'''
class ModuleTests(unittest.TestCase):
    def test_pipeline(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary = task.run_pipeline(DATA/'teaching_records.json', Path(tmp)/'out')
            self.assertEqual(summary['kept'], 6)
            self.assertEqual(summary['input_count'], 12)
            self.assertTrue((Path(tmp)/'out'/'cleaned.csv').exists())
    def test_root_object_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                task.run_pipeline(DATA/'wrong_root.json', Path(tmp)/'out')
            self.assertFalse((Path(tmp)/'out').exists())
    def test_import_has_no_file_writes(self):
        import importlib
        from unittest.mock import patch
        with patch('builtins.open', side_effect=AssertionError('import must not open data')), patch('pathlib.Path.open', side_effect=AssertionError('import must not open data')):
            importlib.reload(task)
''',
'''## 第 1 层
导入已有函数就是复用，不必把函数体复制到新文件。
## 第 2 层
先检查原始 JSON 是否为列表，再让清洗函数处理行。
## 第 3 层
run_pipeline 负责顺序与返回摘要；入口脚本负责用户交互。''',
'自己新建一个脚本，只调用 processing.process_records 处理内存中的三条记录，不进行文件读写。',
'验收还需你阅读三个文件，确认职责分明；自动测试不能证明结构设计一定清晰。')
write('lessons/p07_modules/io_utils.py', '''
from lessons.p01_read.task import load_records
from lessons.p05_clean.task import save_bundle

def load_input(path):
    raise NotImplementedError('TODO: 复用读取函数')

def write_output(cleaned, logs, output_dir):
    raise NotImplementedError('TODO: 复用导出函数')
''')
write('lessons/p07_modules/processing.py', '''
from lessons.p05_clean.task import clean_records

def process_records(records):
    raise NotImplementedError('TODO: 复用清洗函数')
''')

lesson('P08', 'p08_cli', '带预览功能的命令行工具', 'P07', 'argparse、退出状态、stderr、路径',
'''1. 在 build_parser 中定义 --input、--output-dir、--preview，前两者必填。
2. main(argv=None) 解析参数并调用前面的模块。
3. 正常运行打印 JSON 摘要；--preview 只处理并打印，不创建输出目录。
4. 让用户输入错误与代码缺陷有不同处理：只捕获预期文件/数据异常。''',
'''build_parser() -> ArgumentParser。main(argv=None) -> 0 成功或 2 预期错误。预期文件/JSON/根对象/输出已存在错误：stderr 非空且返回2；不要把 NotImplementedError 等编程缺陷吞掉。
成功时 stdout 是一个合法 JSON 摘要（允许缩进），不混其他文字。--help 使用 argparse 默认行为即可。
包根目录运行：py -m lessons.p08_cli.task --input data/teaching_records.json --output-dir output/run01
同一命令追加 --preview 时，output/run01 不应被创建或修改；仍需验证输入根对象。输出不能覆盖输入，沿用 P05 的拒绝覆盖规则。''',
'''
import argparse
import json
import sys
from pathlib import Path
from lessons.p07_modules.task import run_pipeline
from lessons.p07_modules.io_utils import load_input
from lessons.p07_modules.processing import process_records

def build_parser():
    raise NotImplementedError('TODO: 定义命令行参数')

def main(argv=None):
    raise NotImplementedError('TODO: 执行/预览，返回状态码')

if __name__ == '__main__':
    raise SystemExit(main())
''',
'''
import contextlib
import io
import subprocess
import sys
from support import ROOT

class CLITests(unittest.TestCase):
    def test_success_and_preview(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)/'out'
            args = ['--input',str(DATA/'teaching_records.json'),'--output-dir',str(out)]
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(task.main(args+['--preview']), 0)
            self.assertEqual(json.loads(stream.getvalue())['kept'], 6)
            self.assertFalse(out.exists())
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(task.main(args), 0)
            self.assertTrue((out/'summary.json').exists())
    def test_bad_inputs(self):
        for filename in ['absent.json','malformed.json','wrong_root.json']:
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                err = io.StringIO()
                with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
                    code = task.main(['--input',str(DATA/filename),'--output-dir',str(Path(tmp)/'out')])
                self.assertEqual(code, 2)
                self.assertTrue(err.getvalue().strip())
    def test_subprocess_help_and_exit(self):
        result = subprocess.run([sys.executable,'-m','lessons.p08_cli.task','--help'],cwd=str(ROOT),capture_output=True,timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertIn(b'--input', result.stdout)
        result = subprocess.run([sys.executable,'-m','lessons.p08_cli.task','--input','missing.json','--output-dir','output/x'],cwd=str(ROOT),capture_output=True,timeout=10)
        self.assertEqual(result.returncode, 2)
''',
'''## 第 1 层
先让 --help 工作，再接业务函数。终端参数与函数参数是两层接口。
## 第 2 层
main 返回整数，最外层 SystemExit 把整数传给操作系统。
## 第 3 层
预览可调用读取和清洗，但不要调用保存。stdout 留给机器可读 JSON，错误放 stderr。''',
'添加 --limit-preview 参数，仅限制屏幕展示行数，不改变实际清洗结果；自己决定新的展示接口并记录。',
'手动连续执行同一输出命令，确认第二次拒绝覆盖；读懂错误提示后换新输出目录。')

lesson('P09', 'p09_stats', '筛选排序与摘要', 'P05；建议完成 P08', 'sorted、statistics、空结果、参数校验',
'''1. 对清洗记录写闭区间筛选。
2. 写不改变输入的 top_n，最高温度优先，相同温度保持原顺序。
3. 对所有输入记录统计数量、最小值、最大值、平均数。
4. 写 demo 调用 P05 的清洗结果，不手工录入正式输入。''',
'''filter_range(records, low, high) -> 列表，包含 low<=tg_k<=high；low>high 抛 ValueError。
top_n(records,n) -> 最高温前 n 条；n 为整数，负数抛 ValueError，0 返回 []。
summarize(records) -> {'count':int,'min':float或None,'max':float或None,'mean':float或None}。
三个函数不改变输入。已清洗数据的 tg_k 假定为有限数值。
6 条清洗数据中，300–350 K 筛得 EX02、EX10、EX11；此为规则筛选，不是预测。''',
'''
import statistics

def filter_range(records, low, high):
    raise NotImplementedError('TODO: 闭区间筛选')

def top_n(records, n):
    raise NotImplementedError('TODO: 稳定排序后取前 n 条')

def summarize(records):
    raise NotImplementedError('TODO: 统计，明确空输入行为')
''',
'''
class StatsTests(unittest.TestCase):
    def setUp(self):
        self.rows = [{'record_id':'a','tg_k':300.0},{'record_id':'b','tg_k':350.0},{'record_id':'c','tg_k':350.0},{'record_id':'d','tg_k':400.0}]
    def test_boundaries(self):
        old = copy.deepcopy(self.rows)
        self.assertEqual(task.filter_range(self.rows,300,350), self.rows[:3])
        self.assertEqual(task.filter_range(self.rows,1,2), [])
        with self.assertRaises(ValueError): task.filter_range(self.rows,3,2)
        self.assertEqual(self.rows,old)
    def test_ranking(self):
        old = copy.deepcopy(self.rows)
        self.assertEqual([r['record_id'] for r in task.top_n(self.rows,3)], ['d','b','c'])
        self.assertEqual(task.top_n(self.rows,0), [])
        self.assertEqual(len(task.top_n(self.rows,99)),4)
        with self.assertRaises(ValueError): task.top_n(self.rows,-1)
        self.assertEqual(self.rows,old)
    def test_summary(self):
        self.assertEqual(task.summarize(self.rows), {'count':4,'min':300.0,'max':400.0,'mean':350.0})
        self.assertEqual(task.summarize([]), {'count':0,'min':None,'max':None,'mean':None})
''',
'''## 第 1 层
筛选不排序，排序不统计，分别写函数容易检查。
## 第 2 层
sorted 返回新列表；原地 sort 会改变输入。
## 第 3 层
没有样本时先返回约定的空摘要，避免调用 min 或 mean。''',
'新增 median 字段并写手算检查；不要改原 summarize 的接口，另写 summarize_extended。',
'拿纸算 [300,350,350,400] 的结果，解释为什么 count 和筛选后 count 不是同一统计口径。')

lesson('P10', 'p10_pandas', '用 Pandas 对照实现', 'P09；需 pandas', 'DataFrame、数值类型、布尔筛选、结果核对',
'''1. 按 ENVIRONMENT.md 建环境并安装 pandas，先检查解释器。
2. dataframe_report 接受字典列表，构造 DataFrame，显式把 tg_k 转成数值。
3. 给出区间筛选 ID、最高温前 n 的 ID，以及全表统计。
4. 用同一份数据调用 P09，对照所有结果。''',
'''dataframe_report(records, low, high, n) -> {'filtered_ids':list,'top_ids':list,'stats':P09摘要}。
filtered 保留原顺序，top 稳定降序；统计针对全表，非筛选结果。支持 CSV 常见的数值字符串；空输入给空 ID 列表和空摘要。
low>high 或 n<0 抛 ValueError；不可解析/非有限 tg_k 抛 ValueError；不静默删行。
核心筛选和聚合应使用 Pandas，不能只转调 P09 以通过检查。''',
'''
def dataframe_report(records, low, high, n):
    # TODO: 在函数内导入 pandas，让尚未安装库时仍可查看其他关卡。
    raise NotImplementedError('TODO: Pandas 对照实现')
''',
'''
import importlib.util

@unittest.skipUnless(importlib.util.find_spec('pandas'), 'Install pandas for P10')
class PandasTests(unittest.TestCase):
    def test_strings_and_order(self):
        rows=[{'record_id':'a','tg_k':'300'},{'record_id':'b','tg_k':'350'},{'record_id':'c','tg_k':'350'},{'record_id':'d','tg_k':'400'}]
        old=copy.deepcopy(rows)
        result=task.dataframe_report(rows,300,350,3)
        self.assertEqual(result['filtered_ids'],['a','b','c'])
        self.assertEqual(result['top_ids'],['d','b','c'])
        self.assertEqual(result['stats'],{'count':4,'min':300.0,'max':400.0,'mean':350.0})
        self.assertEqual(rows,old)
    def test_empty_and_invalid(self):
        result=task.dataframe_report([],1,2,2)
        self.assertEqual(result,{'filtered_ids':[],'top_ids':[],'stats':{'count':0,'min':None,'max':None,'mean':None}})
        for rows,lo,hi,n in [([],2,1,1),([],1,2,-1),([{'record_id':'x','tg_k':'bad'}],1,2,1),([{'record_id':'x','tg_k':'nan'}],1,2,1)]:
            with self.assertRaises(ValueError): task.dataframe_report(rows,lo,hi,n)
''',
'''## 第 1 层
先处理空列表，再访问列；否则空 DataFrame 可能没有 tg_k 列。
## 第 2 层
查 to_numeric、loc 和 sort_values 的文档。相同值要保持顺序，选择稳定排序。
## 第 3 层
由 Pandas 得到的标量可能是 NumPy 类型；返回普通 Python 数字更方便写 JSON。''',
'从你导出的 CSV 读入，加入空白单元格，说明错误处理与 fillna(0) 的差别。',
'指出标准库版和 Pandas 版各自适合什么场景；自动验收不检查你是否实际用了 Pandas，需要自行/请 AI 审阅。')

lesson('P11', 'p11_plot', '图表与短报告', 'P09；需 matplotlib，P10建议完成', 'figure、axes、单位、文件、信息表达',
'''1. 写 make_plots，对清洗结果生成直方图与按 ID 的柱状图。
2. 图上标注 synthetic teaching data 与 Tg (K)，保存 PNG 后关闭 figure。
3. 添加空输入行为，避免生成没有意义的图。
4. 打开两图，写 100–200 字解释观察和样本局限。''',
'''make_plots(records, output_dir) -> 两个 Path 的列表，顺序为 histogram.png、by_id.png；空输入返回 [] 且不创建输出目录。
输入为清洗后有限数值。非空时创建输出目录；任一目标已存在时抛 FileExistsError，检查发生在绘图前。
函数使用无界面后端或可在无界面环境运行，不调用阻塞的 show。图标题、刻度可读性需人工检查。''',
'''
from pathlib import Path

def make_plots(records, output_dir):
    # TODO: 在导入 pyplot 前按需设置 Agg 后端。
    raise NotImplementedError('TODO: 生成并保存两张图')
''',
'''
import importlib.util

@unittest.skipUnless(importlib.util.find_spec('matplotlib'), 'Install matplotlib for P11')
class PlotTests(unittest.TestCase):
    def test_outputs(self):
        rows=[{'record_id':'a','tg_k':300.0},{'record_id':'b','tg_k':330.0},{'record_id':'c','tg_k':380.0}]
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'figures'
            paths=task.make_plots(rows,out)
            self.assertEqual([Path(p).name for p in paths],['histogram.png','by_id.png'])
            for p in paths:
                self.assertEqual(Path(p).read_bytes()[:8],bytes([137,80,78,71,13,10,26,10]))
                self.assertGreater(Path(p).stat().st_size,500)
            with self.assertRaises(FileExistsError): task.make_plots(rows,out)
    def test_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'empty'
            self.assertEqual(task.make_plots([],out),[])
            self.assertFalse(out.exists())
''',
'''## 第 1 层
先准备 ID 列表和温度列表，再分别画两张图。
## 第 2 层
用 fig.savefig 保存，关闭 figure 防止反复运行累积内存。
## 第 3 层
测试只证明文件像 PNG，不证明图正确；你还需要打开检查单位、标题和数量。''',
'改两种直方图分箱数并比较；补一段说明为什么 6 条教学记录不支持总体规律判断。',
'在 NOTES 中记录实际打开过的图，指出任意一个可能误导读者的表达并修正。')

lesson('P12', 'p12_capstone', '独立完成名字筛选小改版', 'P08、P09；P10/P11可后补', '需求拆分、复用、集成、README',
'''1. 本次固定需求：清洗后按名称关键词和 Tg 区间筛选，再取温度最高的前 N 条。
2. 先在 NOTES 写处理顺序、要复用哪些函数，再实现 select_records。
3. 实现 run_job，把清洗结果与选择结果一起导出，保留原清洗摘要。
4. 写新 CLI 和 MY_README.md，用另一份输入从头运行。''',
'''select_records(records, keyword, low, high, n) -> 已清洗记录列表：先名称匹配，再闭区间，再稳定温度降序取前 n。空白关键词表示不过滤名称；非空匹配规则与 P02 相同。low>high/n<0 抛 ValueError。
run_job(input_path, output_dir, keyword, low, high, n) -> {'input_count':int,'kept':int,'selected':int}。
输出 P05 四文件，加 selected.json（列表）和 selection_summary.json（上述三字段）。任意六文件已存在即提前拒绝；参数无效或 JSON 根不是列表时，不创建输出目录。
CLI 参数 --input、--output-dir 必填；--keyword 默认空、--low/--high 必填 float、--top 默认10。成功 stdout 输出摘要 JSON；预期错误 stderr+退出2，成功0。
主数据取 keyword=demo、low=300、high=350、n=2，应选 EX11、EX10。
本包相较早期任务卡，将“任选改版”具体化为这一项，方便你不再临时等 AI 出题。''',
'''
import argparse
import json
import sys
from pathlib import Path
# TODO: 从前面的关卡导入需要的函数，避免复制实现。

def select_records(records, keyword, low, high, n):
    raise NotImplementedError('TODO: 按约定顺序筛选与排名')

def run_job(input_path, output_dir, keyword, low, high, n):
    raise NotImplementedError('TODO: 完整小工具，六个输出文件')

def main(argv=None):
    raise NotImplementedError('TODO: CLI 参数与反馈')

if __name__ == '__main__':
    raise SystemExit(main())
''',
'''
import contextlib
import io

class CapstoneTests(unittest.TestCase):
    def test_selection_order(self):
        rows=[{'record_id':'a','name':'Alpha','tg_k':310.0},{'record_id':'b','name':'Beta','tg_k':340.0},{'record_id':'c','name':'ALPHABET','tg_k':330.0}]
        old=copy.deepcopy(rows)
        self.assertEqual([r['record_id'] for r in task.select_records(rows,'alpha',300,340,1)],['c'])
        self.assertEqual(len(task.select_records(rows,'  ',300,350,10)),3)
        self.assertEqual(task.select_records(rows,'missing',300,350,10),[])
        self.assertEqual(rows,old)
    def test_real_job(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            summary=task.run_job(DATA/'teaching_records.json',out,'demo',300,350,2)
            self.assertEqual(summary,{'input_count':12,'kept':6,'selected':2})
            selected=json.loads((out/'selected.json').read_text(encoding='utf-8'))
            self.assertEqual([r['record_id'] for r in selected],['EX11','EX10'])
            self.assertTrue((out/'rejected.csv').exists())
            self.assertEqual(json.loads((out/'selection_summary.json').read_text(encoding='utf-8')),summary)
    def test_preflight(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'bad'
            with self.assertRaises(ValueError): task.run_job(DATA/'teaching_records.json',out,'',4,2,1)
            self.assertFalse(out.exists())
            out.mkdir()
            (out/'selected.json').write_text('KEEP',encoding='utf-8')
            with self.assertRaises(FileExistsError): task.run_job(DATA/'teaching_records.json',out,'',1,999,3)
            self.assertEqual([p.name for p in out.iterdir()],['selected.json'])
    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            buf=io.StringIO()
            with contextlib.redirect_stdout(buf):
                code=task.main(['--input',str(DATA/'teaching_records.json'),'--output-dir',str(Path(tmp)/'cli'),'--low','300','--high','350','--top','2'])
            self.assertEqual(code,0)
            self.assertEqual(json.loads(buf.getvalue())['selected'],2)
''',
'''## 第 1 层
先写处理顺序，不要一上来复制整个旧 CLI。
## 第 2 层
本题空关键词表示不过滤，与 P02 的查询约定不同；在组合层做清晰转换。
## 第 3 层
提前检查全部六个文件，不能写完前四个才发现 selected.json 已存在。''',
'再独立加 --sort-by name 或温度最小值筛选中的一个功能，自己写测试和文档；这部分没有预先规定实现。',
'让同学或新 AI 只看 MY_README.md 尝试运行；回看你是否能独立解释每个核心函数。')
write('lessons/p12_capstone/MY_README.md', '''
# 我写的数据处理工具

请亲手补齐：

1. 这个工具解决什么问题，什么不在范围内。
2. 所需 Python/依赖与运行目录。
3. 一条可复制的成功命令。
4. 输入字段、输出文件与筛选顺序。
5. 文件不存在/数据错误/输出已存在时会发生什么。
6. 如何运行检查，哪些事情仍需人工判断。
7. 教学数据局限，我遇到的一个缺陷以及修复方式。
''')

lesson('E01', 'e01_import', '数据导入与来源记录', 'P08；选做', 'CSV、字段映射、可追溯性',
'''1. 先用包内 provider_sample.csv 练导入，它是纯教学数据。
2. 写 adapt_rows 将另一家提供方的列名映射成练习格式。
3. 单位转换复用 P03，目标字段保存为 tg_value（K）和 tg_unit='K'。
4. 整理 SOURCE_NOTES.md，日后换真实数据时再核查来源和表示。''',
'''adapt_rows(rows, source_name) -> 标准字典列表。输入列 sample_id、label、temperature、unit、structure、is_synthetic；教学 CSV 的 is_synthetic 是字符串 true/false，不区分大小写；未知值抛 ValueError，不能默认为真实。
输出 record_id、name、smiles、tg_value（K浮点）、tg_unit='K'、is_synthetic（bool）、source（source_name）。不修改输入。不合法温度或空 ID 抛 ValueError，先不做隔离表。
read_provider(path, source_name) 用 csv.DictReader 并调用 adapt_rows。
实际转接真实数据时，source_name 不是来源证据的替代；本题只教转换，真实数据还需附原始出处、单位依据和许可。''',
'''
import csv
from pathlib import Path
from lessons.p03_units.task import to_kelvin

def adapt_rows(rows, source_name):
    raise NotImplementedError('TODO: 字段映射与明确类型转换')

def read_provider(path, source_name):
    raise NotImplementedError('TODO: CSV 读取与适配')
''',
'''
class ImportTests(unittest.TestCase):
    def test_file(self):
        rows=task.read_provider(DATA/'provider_sample.csv','teaching-provider')
        self.assertEqual(len(rows),3)
        self.assertAlmostEqual(rows[0]['tg_value'],298.15)
        self.assertEqual(rows[0]['tg_unit'],'K')
        self.assertTrue(rows[0]['is_synthetic'])
        self.assertEqual(rows[0]['source'],'teaching-provider')
    def test_no_mutation_and_boolean(self):
        row={'sample_id':'q','label':'Demo','temperature':'310','unit':'K','structure':'CC','is_synthetic':'false'}
        old=copy.deepcopy(row)
        result=task.adapt_rows([row],'test')[0]
        self.assertIs(result['is_synthetic'],False)
        self.assertEqual(row,old)
        with self.assertRaises(ValueError): task.adapt_rows([dict(row,is_synthetic='unknown')],'test')
    def test_empty(self):
        self.assertEqual(task.adapt_rows([],'x'),[])
''',
'''## 第 1 层
CSV 读入后每一格通常是字符串，不要直接 bool('false')。
## 第 2 层
用明确的两个文字值映射布尔类型；其他值拒绝。
## 第 3 层
先对一行建立映射，再把结果追加到新列表。''',
'增加一份不同列名的教学表，用配置字典指定列映射；实际真实数据由你后续选择，本包没有伪造实验来源。',
'写清教学来源与真实来源的区别，不能因字段转换成功就认定数据科学有效。')
write('lessons/e01_import/SOURCE_NOTES.md', '# 来源记录\n\n- 教学/真实：\n- 原始文件：\n- URL/DOI（教学文件可写不适用）：\n- 单位依据：\n- 结构表示：\n- 使用条件：\n- 下载/记录日期：\n- 尚未确认的信息：\n')

lesson('E02', 'e02_rdkit', '结构解析与少量描述符', 'P07；需 rdkit，选做', '第三方对象、失败输入、结构特征',
'''1. 按环境说明安装 RDKit，先尝试解析 CCO。
2. 写 describe_smiles 处理有效、无效和空字符串。
3. 计算原子数、分子量、环数，组织为普通字典。
4. 批量处理 data/smiles_examples.json 并保存结果。''',
'''describe_smiles(text) -> {'valid':bool,'num_atoms':int或None,'mol_wt':float或None,'num_rings':int或None}。
非字符串、空白、解析失败均返回 valid=False，其余三项 None；合法时用 RDKit 的分子图和描述符计算，不用字符计数替代原子数。
只处理提供的简单分子示例。含 * 的聚合物重复单元规范和科学意义不在本关验收范围；继续做真实项目时需要另行核查。''',
'''
def describe_smiles(text):
    # TODO: 函数内导入 RDKit，处理解析失败。
    raise NotImplementedError('TODO: 合法性和描述符')
''',
'''
import importlib.util

@unittest.skipUnless(importlib.util.find_spec('rdkit'), 'Install rdkit for E02')
class RDKitTests(unittest.TestCase):
    def test_simple(self):
        result=task.describe_smiles('CCO')
        self.assertIs(result['valid'],True)
        self.assertEqual(result['num_atoms'],3)
        self.assertEqual(result['num_rings'],0)
        self.assertGreater(result['mol_wt'],0)
    def test_ring(self):
        result=task.describe_smiles('c1ccccc1')
        self.assertEqual(result['num_atoms'],6)
        self.assertEqual(result['num_rings'],1)
    def test_invalid(self):
        expected={'valid':False,'num_atoms':None,'mol_wt':None,'num_rings':None}
        for value in [None,'','   ','not_a_smiles']:
            self.assertEqual(task.describe_smiles(value),expected)
''',
'''## 第 1 层
先检查空值，再调用 MolFromSmiles；失败可能返回 None。
## 第 2 层
从 Chem 和 Descriptors 的官方示例开始，先只验证一个分子。
## 第 3 层
图的原子数不等于字符串长度，括号、数字和多字符元素会打破这种对应。''',
'画出两种结构，并用程序比较它们的原子数和环数；不解释成 Tg 因果规律。',
'说明 MolWt 在这里是有限分子的描述符，不能直接当成整条聚合物链的分子量。')

lesson('E03', 'e03_ml', '离线回归 API 练习', 'P09；需 scikit-learn，选做', 'X/y、训练测试、基线、误差',
'''1. 使用包内 toy_regression.json，不需要下载真实数据。
2. 只取 x1、x2 为输入，target 为人为教学标签，ID 和标签不放入 X。
3. 固定 random_state=42，80/20 划分；仅在训练部分拟合 Dummy 和一个 RandomForestRegressor。
4. 算测试 RMSE，返回指标与划分 ID；不要反复挑种子。''',
'''train_and_evaluate(rows) -> {'baseline_rmse':float,'model_rmse':float,'n_train':int,'n_test':int,'train_ids':list,'test_ids':list}。
采用 train_test_split(test_size=0.2,random_state=42)。RandomForestRegressor 固定 n_estimators=50, random_state=42, n_jobs=1，其余默认。DummyRegressor 使用 mean。
不预设模型必须超过某个分数；训练数据需至少10行、ID唯一，x1/x2/target为有限数值，违约抛 ValueError。本关可不泛化其他类型。
全部数据是确定性生成的数值教学题，**不是聚合物结构或实验 Tg**。通过本关只说明掌握调用流程；将来用于材料时再采用真实结构特征、实验标签、分组划分与科学评估。''',
'''
def train_and_evaluate(rows):
    # TODO: 在函数内导入 sklearn；自己建立 X/y、划分、拟合与评价。
    raise NotImplementedError('TODO: 基线和随机森林回归')
''',
'''
import importlib.util

@unittest.skipUnless(importlib.util.find_spec('sklearn'), 'Install scikit-learn for E03')
class MLTests(unittest.TestCase):
    def test_metrics_and_split(self):
        rows=read_fixture('toy_regression.json')
        old=copy.deepcopy(rows)
        result=task.train_and_evaluate(rows)
        self.assertEqual(result['n_train'],48)
        self.assertEqual(result['n_test'],12)
        self.assertEqual(len(result['train_ids']),48)
        self.assertEqual(len(result['test_ids']),12)
        self.assertFalse(set(result['train_ids']) & set(result['test_ids']))
        self.assertEqual(set(result['train_ids']) | set(result['test_ids']), {r['record_id'] for r in rows})
        self.assertEqual(rows,old)
        # 独立核算基线，防止直接编造指标或偷用测试标签均值。
        from sklearn.model_selection import train_test_split
        train,test=train_test_split(rows,test_size=0.2,random_state=42)
        self.assertEqual(result['test_ids'],[r['record_id'] for r in test])
        avg=sum(r['target'] for r in train)/len(train)
        expected=math.sqrt(sum((r['target']-avg)**2 for r in test)/len(test))
        self.assertAlmostEqual(result['baseline_rmse'],expected,places=7)
        self.assertTrue(math.isfinite(result['model_rmse']))
        self.assertGreaterEqual(result['model_rmse'],0)
    def test_repeat_and_invalid(self):
        rows=read_fixture('toy_regression.json')
        a=task.train_and_evaluate(rows)
        b=task.train_and_evaluate(rows)
        self.assertAlmostEqual(a['model_rmse'],b['model_rmse'])
        with self.assertRaises(ValueError): task.train_and_evaluate(rows[:3])
        with self.assertRaises(ValueError): task.train_and_evaluate(rows+[rows[0]])
''',
'''## 第 1 层
先用一行手写出 X 的两个元素和 y；确认 target 没有进入输入。
## 第 2 层
划分时保持行身份，预测后可以知道每个值对应哪个 ID。
## 第 3 层
RMSE 可用 mean_squared_error 后开平方，不必依赖特定版本的 squared 参数。''',
'只在训练集内部再留一份验证集比较两种树深度，最终测试仍只用于报告；把额外选择写清楚。',
'代码审阅确认确实训练 RF、没有在测试集 fit；自动检查不能代替完整泄漏审计。')

lesson('E04', 'e04_security', '本地日志与文件完整性', 'P08；选做，标准库', 'datetime、字典计数、hashlib、分块读取',
'''1. 从 synthetic_events.json 读取自行构造的本地事件日志。
2. 按成功状态和时间闭区间筛出失败事件，统计每个虚构用户的次数。
3. 写 sha256_file 分块读取文件，比较修改前后的摘要。
4. 复用 CLI 思路，给自己的日志工具添加入口。''',
'''failed_counts(events,start,end) -> user_id到失败次数的字典。事件字段 timestamp（带时区ISO字符串）、user_id、success（bool）。start/end也是带时区ISO字符串；使用 datetime 进行比较，start>end或缺时区抛 ValueError。成功用户不列入结果，空结果 {}。
sha256_file(path) -> 64字符小写十六进制摘要；文件不存在保留 FileNotFoundError。请分块读取，不要求一次把整个文件放内存。
只用本地虚构日志，不需要网络扫描或任何真实账号。''',
'''
from datetime import datetime
import hashlib
from pathlib import Path

def failed_counts(events, start, end):
    raise NotImplementedError('TODO: 时间过滤和失败次数')

def sha256_file(path):
    raise NotImplementedError('TODO: 分块读取并计算摘要')
''',
'''
class SecurityTests(unittest.TestCase):
    def test_counts_and_boundaries(self):
        rows=read_fixture('synthetic_events.json')
        self.assertEqual(task.failed_counts(rows,'2026-01-01T00:00:00+00:00','2026-01-01T01:00:00+00:00'),{'demo_u1':2,'demo_u2':1})
        self.assertEqual(task.failed_counts([], '2026-01-01T00:00:00+00:00','2026-01-01T01:00:00+00:00'),{})
        with self.assertRaises(ValueError): task.failed_counts([], '2026-01-02T00:00:00+00:00','2026-01-01T00:00:00+00:00')
        with self.assertRaises(ValueError): task.failed_counts([], '2026-01-01T00:00:00','2026-01-02T00:00:00')
    def test_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'sample.bin'
            p.write_bytes(b'abc')
            self.assertEqual(task.sha256_file(p),'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
            old=task.sha256_file(p)
            p.write_bytes(b'abcd')
            self.assertNotEqual(task.sha256_file(p),old)
            with self.assertRaises(FileNotFoundError): task.sha256_file(Path(tmp)/'absent')
''',
'''## 第 1 层
先解析时间，再比较；不要混用没有时区的日期对象。
## 第 2 层
字典的 get(user,0) 可以帮助计数；success 必须按布尔值判断。
## 第 3 层
hashlib 对象支持多次 update，最后取 hexdigest。''',
'生成自己的一份虚构日志，加入不同UTC偏移但代表同一时刻的事件，验证时间比较。',
'解释哈希能帮助发现文件变化，但没有可信原始摘要时并不能自动证明文件来源可信。')

# Data are teaching inputs only, never purported experimental records.
source = WORKSPACE / 'python_practice' / 'data' / 'teaching_records.json'
write('data/teaching_records.json', source.read_text(encoding='utf-8'))
write('data/empty.json', '[]')
write('data/wrong_root.json', '{"records": []}')
write('data/malformed.json', '[{"record_id": "broken",]')
write('data/provider_sample.csv', '''
sample_id,label,temperature,unit,structure,is_synthetic
PV01,demo_provider_one,25,C,CCO,true
PV02,demo_provider_two,310,K,CC,true
PV03,demo_provider_three,-20,C,CCC,true
''')
write('data/smiles_examples.json', json.dumps(['CCO','CC','c1ccccc1','not_a_smiles',''],indent=2))
toy = []
for i in range(60):
    x1=(i % 15)/3.0
    x2=((i*7)%19)/4.0
    toy.append(dict(record_id='SYN%03d'%i,x1=x1,x2=x2,target=round(2*x1-0.5*x2+(i%3-1)*0.1,5),is_synthetic=True))
write('data/toy_regression.json',json.dumps(toy,indent=2))
events=[]
for minute,user,success in [(0,'demo_u1',False),(10,'demo_u1',True),(20,'demo_u2',False),(60,'demo_u1',False),(61,'demo_u2',False)]:
    events.append(dict(timestamp='2026-01-01T%02d:%02d:00+00:00'%(minute//60,minute%60),user_id=user,success=success,is_synthetic=True))
write('data/synthetic_events.json',json.dumps(events,indent=2))
write('data/README.md', '''
# 教学输入清单

所有记录由人工或确定性公式构造，用来练程序，不是实测材料数据。

| 文件 | 用途 |
|---|---|
| teaching_records.json | 主线12行数据：7行格式/数值合法，5行失败，去重后6行 |
| empty.json | 合法空列表，与损坏文件不同 |
| wrong_root.json | JSON合法但根对象不是列表 |
| malformed.json | 故意损坏的JSON，解析失败是预期 |
| provider_sample.csv | E01字段映射用的另一种教学格式 |
| smiles_examples.json | E02简单结构字符串，非真实聚合物属性配对 |
| toy_regression.json | E03的60条数值教学数据，target不是Tg |
| synthetic_events.json | E04虚构用户的本地日志，带时区 |

主线数据的温度、名称和SMILES不构成真实性质关系。原始数据不要直接改动；独立变式用你自己的新文件。
''')

write('manifest.json',json.dumps(LESSONS,ensure_ascii=False,indent=2))
write('check.py', '''
"""Provided runner: check one lesson, prerequisites, or list the route."""
import argparse
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parent

def main(argv=None):
    parser=argparse.ArgumentParser(description='Check handwritten exercise code. Unfinished stubs are expected to fail.')
    parser.add_argument('lesson',nargs='?',help='P01..P12 or E01..E04')
    parser.add_argument('--list',action='store_true')
    parser.add_argument('--through',action='store_true',help='Run P01 through the selected P lesson')
    args=parser.parse_args(argv)
    items=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    index={row['id']:row for row in items}
    if args.list:
        for row in items: print(row['id']+'  '+row['title']+'  ['+row['folder']+']')
        return 0
    code=(args.lesson or '').upper()
    if code not in index: parser.error('Choose P01..P12 or E01..E04, or use --list')
    if args.through and not code.startswith('P'): parser.error('--through applies only to P lessons')
    selected=[row for row in items if row['id'].startswith('P') and row['id']<=code] if args.through else [index[code]]
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    for row in selected:
        module=row['folder'].replace('/','.')
        suite.addTests(loader.loadTestsFromName(module+'.test_task'))
        if row['id']=='P06': suite.addTests(loader.loadTestsFromName(module+'.test_student'))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    if result.skipped:
        print('INCOMPLETE: skipped checks (usually missing optional dependencies). This is not a pass.')
    if not result.wasSuccessful():
        print('NOT FINISHED: use the first traceback, lesson contract and HINTS.md. Unfilled TODOs should fail.')
    elif not result.skipped:
        print('AUTOMATED CHECKS PASSED. Also complete the manual review and independent variation.')
    return 0 if result.wasSuccessful() and not result.skipped else 1

if __name__=='__main__':
    raise SystemExit(main())
''')

write('README.md', '''
# 亲手写 Python 全路线练习包

这是一套可以独立解压使用的练习包，面向已经会基础 Python 的信息安全大二学生。项目背景来自聚合物数据处理，但主要目标是你自己写代码。包内提供 12 个主线关卡、4 个选做方向，以及完整输入、骨架、验收和提示；核心实现留给你。

**从此包开始执行即可。旧文件夹 python_practice 和之前的指南可留作参考，不必再同时维护两份练习。** 如果你已经写过第一题，可以把自己的实现移入 P01，按本包接口补齐 preview_records。

## 怎么开始

1. 把整个文件夹放在你喜欢的位置，或解压同名 ZIP。
2. 用编辑器打开 python_handson_pack 文件夹；终端也切到这个目录。
3. 先运行下面的清单命令，确认 Python 可用。
4. 打开 lessons/p01_read/README.md，亲手填写同目录 task.py。
5. 写完一小步就运行本关测试；不要先把所有文件读一遍。

```powershell
py check.py --list
py check.py P01
```

本机若使用 python 命令，替换 py 即可。P01 的展示入口是：

```powershell
py -m lessons.p01_read.task
```

核心代码未写前出现 NotImplementedError 或失败测试是正常的。测试是目标，不是已经替你做完的程序。缺少可选库导致 skip 也不算通过。

## 每关打开哪些文件

| 文件 | 用法 |
|---|---|
| README.md | 题目、步骤、函数输入输出、命令、变式 |
| task.py | 你主要写代码的位置；P06 是故意有缺陷的程序 |
| test_task.py | 已提供验收用例，可读来理解预期，不靠改测试通关 |
| HINTS.md | 卡住再逐层打开，先看第一层 |
| variations.py | 独立变式，由你自己写输入与检查 |
| NOTES.md | 简短记录运行结果和错误原因 |

P06 另外需要亲手补 test_student.py；P07 需要补三个模块；P12 需要补自己的使用说明。

## 完整路径

| 阶段 | 关卡 | 最终写出的程序 | 停下来的成果 |
|---|---|---|---|
| A | P01读取 → P02查询 → P03转换 → P04校验 | 能解释错误的数据检查器 | 约4–8次练习 |
| B | P05导出 → P06调试 → P07模块 → P08命令行 | 可复用的数据清洗工具 | 再约6–10次练习 |
| C | P09统计 → P10Pandas → P11绘图 → P12小改版 | 筛选、分析、导出的个人工具 | 再约6–10次练习 |
| 选做 | E01导入、E02RDKit、E03回归、E04安全日志 | 选择一个方向深入 | 不要求全做 |

每次约45–90分钟，估计难度因人而异；时间表不是截止日期。你可以停在任一阶段，或者在 P08 后先做 E04。机器学习不是通关条件。

## 要保持的练习方式

先写三行思路，自己编码20–30分钟，再看提示或问AI；完成后换一个输入、做一个小变式，并解释为什么这样写。完整答案只在你明确需要时索取；看完应关掉答案再重写一个变式。

前九关只需标准库。P10/P11和部分扩展才安装对应库，见 [环境说明](ENVIRONMENT.md)。详细顺序见 [路线与能力](ROADMAP.md)，AI辅导方式见 [AI助教约定](AI_TUTOR.md)，状态记到 [学习进度](PROGRESS.md)。

数据全部是教学样例，不能用于材料预测效果宣传。自动测试覆盖核心行为，图表阅读、代码质量、是否独立完成仍需要人工判断。原科研题的真实来源和科学评估是将来的升级方向。
''')
write('ENVIRONMENT.md', '''
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
''')

write('ROADMAP.md', '''
# 路线与能力检查

## 不必一次完成的长期路线

第1轮以写通为目标，第2轮以错误处理和复用为目标，第3轮独立改需求。每关README提供具体步骤，按步骤拆成多次练习，不要一次让AI生成整关。

| 关卡 | 开始前补的最少知识 | 关卡完成后的提问 |
|---|---|---|
| P01 | json.load、with、Path、列表切片 | load与loads有何区别？返回值是什么？ |
| P02 | get、casefold、列表追加 | 重复ID为什么不应只返回一个对象？ |
| P03 | float、isfinite、ValueError | 为什么bool和NaN要单独处理？ |
| P04 | enumerate、局部异常 | 如何收集两个错误而不提前结束？ |
| P05 | csv.DictWriter、复制、去重 | 如何证明没有丢行或改掉原始数据？ |
| P06 | traceback、unittest | 测试能否在修复前失败、修复后通过？ |
| P07 | import与模块入口 | 为什么导入不该自动生成文件？ |
| P08 | argparse、stdout/stderr | 程序退出状态与返回字符串有何区别？ |
| P09 | sorted/key、均值、空集合 | 空平均数与0为什么不同？ |
| P10 | DataFrame、布尔筛选 | 库做了什么，标准库版如何验证它？ |
| P11 | axes、标签、保存图 | 图能打开是否代表内容就正确？ |
| P12 | 需求分解、集成、README | 只看自己的说明能否在另一目录运行？ |

## 三种练习深度

1. 必做：完成骨架和本关自动测试。
2. 掌握：独立变式写出代码，自己构造输入，解释结果。
3. 深化：找一个缺陷、补一个有价值的测试，或让他人只按你的说明使用。

不要因为测试变绿就跳过理解。也不要为追求完美而在第一关写复杂框架。

## 如果卡住

- 语法问题：把完整traceback缩减到最小例子，查当前调用的函数。
- 不知道怎么开始：在注释里写“读取/检查/计算/保存”，先实现其中一步。
- 结果不符：打印中间变量的值与类型，用3条输入手算。
- 依赖未完成：返回题目指定的前置关，不临时复制AI的整套实现。
- 测试看不懂：先看assert的输入和期望；可请AI翻译测试，不要立即索要答案。
- 包安装失败：继续标准库题或E04；安装问题不阻止你练代码。

## 完成主线后如何选择

喜欢数据：E01，增加字段映射和来源记录。
喜欢材料：E02，先学结构解析；之后若做真实Tg项目，再研究实验数据、重复单元和评价。
喜欢算法：E03，用离线数值数据理解训练/预测；不要把教学分数当科研结果。
喜欢本专业：E04，把同样的能力迁移到日志和文件完整性。

E01–E04都有骨架、输入与测试，所以现在就已准备好；是否做、何时做由你决定。进一步完整科研项目不是本训练包的必做终点。
''')
write('AI_TUTOR.md', '''
# AI 助教约定

把下面这段与当前关卡README、你的task.py和报错一起发给其他AI即可。

```text
我基本会Python简单语法，主要目标是亲手写代码，提高独立实现和调试能力。
现在使用 python_handson_pack，当前关卡是：____。
请以当前关卡README的函数契约为准，只辅导这一小步。

我已完成：____。
卡住的位置：____。
运行命令和完整报错：____。

请先让我解释思路，再给一个最小提示，不主动给整份完整实现。
需要例子时用不同输入和一个小片段，不替我完成所有函数。
我贴代码后，先检查正确性，再最多指出两项可读性问题。
保留我正确且简单的写法，不擅自换成复杂框架。
不要改测试来让错误答案通过，也不要硬编码样例ID和数量。
测试不覆盖的需求也需要按README实现。
没有执行就写明未执行；不要虚构运行结果或研究结论。
最后给一个不依赖答案的变式，让我独立改代码。
只有我明确索要完整示例时，才提供完整答案。
```

## 求助可以具体一点

- “帮我解释这条traceback最后三行，不要修改代码。”
- “只检查我的函数会不会改变原始列表。”
- “给一个会让我的程序失败的输入，让我自己修。”
- “指出最优先的一个问题，暂时不重构。”
- “我能跑通了，请让我口头解释返回值，再出一道小变式。”

## 何时可以看完整示例

已经尝试、知道具体卡点但连续提示仍无法推进时，可以看一个完整函数。随后关掉它，自己改一个新需求，重新运行并解释。不要把AI生成的行数当作自己的练习量。

## 交接只需五项

当前关卡、已有代码、输入样例、准确命令和结果、你想获得的帮助。完整科研资料不是本阶段每次求助的前置材料。
''')
write('PROGRESS.md', '# 我的代码练习进度\n\n所有练习起始状态均为未开始；骨架和检查器已提供不等于我已完成。\n\n|关卡|任务|状态|实际命令与结果|独立变式|能解释的内容|\n|---|---|---|---|---|---|\n' + '\n'.join('|%s|%s|未开始|—|—|—|'%(r['id'],r['title']) for r in LESSONS) + '\n\n状态建议：未开始 / 在写 / 需提示 / 检查通过 / 能独立修改。选做不做也无需补齐。\n')
write('CONTRACTS.md', '''
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
''')
write('RESOURCES.md', '''
# 按需查阅的官方资料

只读解决当前问题的段落，不要求先读完整本手册。在线文档会更新，第三方库按实际安装版本查API。

- P01–P05：[Python中文教程](https://docs.python.org/zh-cn/3/tutorial/index.html)，查数据结构、输入输出、异常。
- P06：[unittest](https://docs.python.org/zh-cn/3/library/unittest.html)，先看基本示例、assertEqual、assertRaises。
- P08：[argparse](https://docs.python.org/zh-cn/3/library/argparse.html)，先看ArgumentParser、add_argument、parse_args。
- P10：[Pandas入门](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)，查筛选、派生列、统计。
- P11：[Matplotlib教程](https://matplotlib.org/stable/tutorials/index.html)，查图对象、坐标标签和保存。
- E02：[RDKit入门](https://www.rdkit.org/docs/GettingStartedInPython.html)，查分子读取和描述符；[安装说明](https://www.rdkit.org/docs/Install.html)。
- E03：[scikit-learn常见陷阱](https://scikit-learn.org/stable/common_pitfalls.html)，重点看一致预处理与数据泄漏。
- E03进阶：[官方教学数据说明](https://scikit-learn.org/stable/datasets/toy_dataset.html)，将来可换一种公开教学数据；本包的E03已自带人工数据，不依赖下载。

本包的练习分解、接口和教学数据是为你的编程目标设计的，不是上述文档规定的课程或科学规范。
''')
write('.gitignore', '__pycache__/\n*.pyc\n.venv/\noutput/\n')
write('PACKAGE_STATUS.md', '''
# 包的状态

这是练习材料，不是已完成的课程答案。任务函数大多有TODO，P06故意包含错误。
主线与扩展的数据、接口、运行器、用例和提示已经提供；学习者仍需亲手实现并验收。
测试不会因为骨架已存在而自动通过。开发侧检查记录见PACKAGE_QA.md（打包时生成）。
''')


def make_archive():
    archive=WORKSPACE/'python_handson_pack.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and '.venv' not in p.parts and 'output' not in p.relative_to(ROOT).parts:
                z.write(p,Path(ROOT.name)/p.relative_to(ROOT))
    return archive


if __name__=='__main__':
    print('Generated %d lessons in %s'%(len(LESSONS),ROOT))
    print('Archive: %s'%make_archive())
