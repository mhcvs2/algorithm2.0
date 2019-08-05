import unittest


class TwoStackQueue(object):

    def __init__(self):
        self._stack_push = []
        self._stack_pop = []

    def _push_to_pop(self):
        if len(self._stack_pop) == 0:
            while len(self._stack_push) > 0:
                self._stack_pop.append(self._stack_push.pop())

    def add(self, value):
        self._stack_push.append(value)
        self._push_to_pop()

    def poll(self):
        if len(self._stack_push) == 0 and len(self._stack_pop) == 0:
            raise Exception("queue is empty")
        self._push_to_pop()
        return self._stack_pop.pop()

    def peek(self):
        if len(self._stack_push) == 0 and len(self._stack_pop) == 0:
            raise Exception("queue is empty")
        self._push_to_pop()
        return self._stack_pop[-1]


class TwoStackQueueTest(unittest.TestCase):

    def test1(self):
        queue = TwoStackQueue()
        queue.add(1)
        queue.add(2)
        queue.add(3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.poll(), 1)
        self.assertEqual(queue.poll(), 2)
        self.assertEqual(queue.poll(), 3)
        with self.assertRaises(Exception):
            queue.poll()
