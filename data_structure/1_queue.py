from unittest import TestCase


class Queue(object):

    def __init__(self, size):
        self._size = size + 1
        self._data = [0] * self._size
        self._head = 0
        self._tail = 0

    def is_empty(self):
        return self._head == self._tail

    def is_full(self):
        return (self._tail + 1) % self._size == self._head

    def add(self, item):
        if self.is_full():
            raise Exception("is full")
        self._data[self._tail] = item
        self._tail = (self._tail + 1) % self._size

    def get(self):
        if self.is_empty():
            return None
        res = self._data[self._head]
        self._head = (self._head + 1) % self._size
        return res


class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue2(object):

    def __init__(self, size):
        self._size = size
        self._len = 0
        self._head = None

    def is_full(self):
        return self._len == self._size

    def is_empty(self):
        return self._len == 0

    def add(self, item):
        if self.is_full():
            raise Exception("is full")
        if not self._head:
            self._head = Node(item)
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = Node(item)
        self._len += 1

    def get(self):
        if self.is_empty():
            return None
        res = self._head.data
        self._head = self._head.next
        self._len -= 1
        return res


class TestQueue(TestCase):

    def test1(self):
        q = Queue2(10)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.add(1)
        q.add(2)
        self.assertFalse(q.is_empty())
        self.assertEqual(1, q.get())
        self.assertEqual(2, q.get())
        self.assertTrue(q.is_empty())
