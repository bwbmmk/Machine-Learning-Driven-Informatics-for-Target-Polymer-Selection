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
