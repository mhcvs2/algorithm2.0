import unittest
from ch2.base import BaseUtils


def reverse(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def reverse_double(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next
    return pre


class TestReverse(unittest.TestCase):

    def _compare(self, source, expected):
        res = reverse(source)
        BaseUtils.print_single(res)
        self.assertTrue(BaseUtils.is_equal(expected, res))

    def test_reverse(self):
        self._compare(BaseUtils.gen_single([1, 2, 3, 4]),
                      BaseUtils.gen_single([4, 3, 2, 1]))

    def _compare_double(self, source, expected):
        res = reverse_double(source)
        BaseUtils.print_double(res)
        self.assertTrue(BaseUtils.is_double_equal(expected, res))

    def test_reverse_double(self):
        self._compare_double(BaseUtils.gen_double([1, 2, 3, 4]),
                      BaseUtils.gen_double([4, 3, 2, 1]))
