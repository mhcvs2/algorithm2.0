from unittest import TestCase


class PriorityQueue(object):

    def __init__(self, size=1000):
        self._data = [0] * size
        self._size = size
        self._len = 0

    def is_full(self):
        return self._len == self._size

    def is_empty(self):
        return self._len == 0

    def add(self, x):
        if self.is_full():
            raise Exception("is full")
        i = self._len
        self._len += 1
        while i > 0:
            p = int((i-1)/2)
            if self._data[p] <= x:
                break
            self._data[i] = self._data[p]
            i = p
        self._data[i] = x

    def get(self):
        if self.is_empty():
            return None
        res = self._data[0]
        i = 0
        x = self._data[self._len-1]
        self._len -= 1
        while 2 * i + 1 < self._len:
            a = 2 * i + 1
            b = 2 * i + 2
            if b < self._len and self._data[b] < self._data[a]:
                a = b
            if x < self._data[a]:
                break
            self._data[i] = self._data[a]
            i = a
        self._data[i] = x
        return res

    @property
    def data(self):
        return self._data[:self._len]


class TestQueue(TestCase):

    def test1(self):
        q = PriorityQueue(10)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.add(10)
        q.add(8)
        q.add(1)
        q.add(2)
        q.add(3)
        # [1, 2, 8, 10, 3]
        print(q.data)
        self.assertFalse(q.is_empty())
        self.assertEqual(1, q.get())
        self.assertEqual(2, q.get())

