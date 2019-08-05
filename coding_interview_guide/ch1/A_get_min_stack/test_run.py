import unittest
from a import GetMinStack
from b import GetMinStack2


class GetMinStackTest(unittest.TestCase):

    def _test(self, stack):
        stack.push(3)
        self.assertEqual(stack.get_min(), 3)
        stack.push(4)
        self.assertEqual(stack.get_min(), 3)
        stack.push(5)
        self.assertEqual(stack.get_min(), 3)
        stack.push(1)
        self.assertEqual(stack.get_min(), 1)
        stack.push(2)
        self.assertEqual(stack.get_min(), 1)
        stack.push(1)
        self.assertEqual(stack.get_min(), 1)
        res = stack.pop()
        self.assertEqual(res, 1)
        self.assertEqual(stack.get_min(), 1)
        res = stack.pop()
        self.assertEqual(res, 2)
        self.assertEqual(stack.get_min(), 1)
        res = stack.pop()
        self.assertEqual(res, 1)
        self.assertEqual(stack.get_min(), 3)

    def test1(self):
        stack = GetMinStack()
        self._test(stack)

    def test2(self):
        stack = GetMinStack2()
        self._test(stack)
