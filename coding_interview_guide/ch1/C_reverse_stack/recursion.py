# encoding: utf-8
import unittest


def get_and_remove_last_element(stack):
    """ 获取并移除栈底的元素 """
    result = stack.pop()
    if len(stack) == 0:
        return result
    last = get_and_remove_last_element(stack)
    stack.append(result)
    return last


def reverse_stack(stack):
    """ 将栈逆序 """
    if len(stack) == 0:
        return
    i = get_and_remove_last_element(stack)
    reverse_stack(stack)
    stack.append(i)


class ReverseStackTest(unittest.TestCase):

    def test_reverse(self):
        stack = [1, 2, 3, 4, 5]
        reverse_stack(stack)
        self.assertEqual(stack, [5, 4, 3, 2, 1])
