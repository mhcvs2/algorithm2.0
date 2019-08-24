# encoding: utf-8
import unittest
from ch2.base import BaseUtils


def reverse_part(head, f, t):
    n = 0
    cur = head
    pre_f = None
    post_t = None
    # 获取指定位置的元素
    while cur is not None:
        n += 1
        pre_f = cur if n == f-1 else pre_f
        post_t = cur if n == t+1 else post_t
        cur = cur.next
    if f >= t or f < 1 or t > n:
        return head
    # 从指定元素到指定元素反转
    pre = head if pre_f is None else pre_f.next
    cur = pre.next
    pre.next = post_t
    _next = None
    while cur is not post_t:
        _next = cur.next
        cur.next = pre
        pre = cur
        cur = _next
    if pre_f is not None:
        pre_f.next = pre
        return head
    return pre


class TestReversePart(unittest.TestCase):

    def _compare(self, source_list, f, t, expected):
        source = BaseUtils.gen_single(source_list)
        res = reverse_part(source, f, t)
        expected = BaseUtils.gen_single(expected)
        success = BaseUtils.is_equal(res, expected)
        if not success:
            print('source---------------')
            BaseUtils.print_single(BaseUtils.gen_single(source_list))
            print('reverse result-------------')
            BaseUtils.print_single(res)
            print('expected------------------')
            BaseUtils.print_single(expected)
        self.assertTrue(success)

    def test_reverse_part(self):
        self._compare(
            [1, 2, 3, 4, 5],
            2, 4,
            [1, 4, 3, 2, 5]
        )
        self._compare(
            [1, 2, 3],
            1, 3,
            [3, 2, 1]
        )
        self._compare(
            [1, 2, 3, 4],
            2, 3,
            [1, 3, 2, 4]
        )
