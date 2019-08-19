import unittest
from .base import BaseUtils


class TestSingle(unittest.TestCase):

    def setUp(self):
        self.datas = [None]
        for l in range(2, 10):
            self.datas.append(BaseUtils.gen_single(list(range(1, l))))

    def print_datas(self):
        for d in self.datas:
            BaseUtils.print_single(d)
