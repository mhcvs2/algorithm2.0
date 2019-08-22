# encoding: utf-8
import math
import unittest
from ch2.base import BaseUtils


def delete_a_b(head, a, b):
    if a < 1 or a > b:
        return head
    l = BaseUtils.get_length(head)
    if l == 0:
        return head
    to_delete_index = math.ceil(l * a / b)
    if to_delete_index == 1:
        return head.next
    cur = head
    while to_delete_index > 2:
        cur = cur.next
        to_delete_index -= 1
    cur.next = cur.next.next
    return head


class TestDeleteAB(unittest.TestCase):

    def _compare(self, source, a, b, expected):
        """
        :param source: 要转换的原始链表
        :param a: 值a
        :param b: 值b
        :param expected: 执行delete_a_b之后期望的结果链表
        :return:
        """
        self.assertTrue(BaseUtils.is_equal(delete_a_b(source, a, b), expected))

    def test_delete_a_b(self):
        self._compare(BaseUtils.gen_single([1, 2, 3, 4, 5]),
                      0, 5,
                      BaseUtils.gen_single([1, 2, 3, 4, 5]))
        self._compare(BaseUtils.gen_single([1, 2, 3, 4, 5]),
                      1, 5,
                      BaseUtils.gen_single([2, 3, 4, 5]))
        self._compare(BaseUtils.gen_single([1, 2, 3, 4, 5]),
                      2, 5,
                      BaseUtils.gen_single([1, 3, 4, 5]))
        self._compare(BaseUtils.gen_single([1, 2, 3, 4, 5]),
                      5, 5,
                      BaseUtils.gen_single([1, 2, 3, 4]))
        self._compare(BaseUtils.gen_single([1, 2, 3, 4, 5]),
                      6, 5,
                      BaseUtils.gen_single([1, 2, 3, 4, 5]))
        self._compare(BaseUtils.gen_single([1, 2, 3, 4, 5, 6, 7]),
                      5, 7,
                      BaseUtils.gen_single([1, 2, 3, 4, 6, 7]))
        self._compare(BaseUtils.gen_single([1, 2, 3, 4, 5, 6, 7]),
                      5, 6,
                      BaseUtils.gen_single([1, 2, 3, 4, 5, 7]))
