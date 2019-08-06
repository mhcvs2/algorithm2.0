import unittest


def sort_stack_by_stack(stack):
    help = []
    while len(stack) > 0:
        cur = stack.pop()
        while len(help) > 0 and help[-1] < cur:
            stack.append(help.pop())
        help.append(cur)
    while len(help) > 0:
        stack.append(help.pop())


class TestSortStackByStack(unittest.TestCase):

    def test_sort(self):
        stack = [2, 5, 1, 3, 6]
        sort_stack_by_stack(stack)
        self.assertEqual([1, 2, 3, 5, 6], stack)
