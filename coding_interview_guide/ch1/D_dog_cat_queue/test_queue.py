import unittest
from .model import Cat, Dog
from .queue import DogCatQueue


class TestQueue(unittest.TestCase):

    def test1(self):
        q = DogCatQueue()
        q.add(Cat())
        q.add(Dog())
        self.assertEqual(False, q.is_empty)
        self.assertEqual(False, q.is_cat_empty)
        self.assertEqual(False, q.is_dog_empty)
        p1 = q.poll_all()
        self.assertIsInstance(p1, Cat)
        p2 = q.poll_all()
        self.assertIsInstance(p2, Dog)

    def test2(self):
        q = DogCatQueue()
        q.add(Cat())
        q.add(Dog())
        p1 = q.poll_dog()
        self.assertIsInstance(p1, Dog)
        self.assertEqual(True, q.is_dog_empty)
        p2 = q.poll_cat()
        self.assertIsInstance(p2, Cat)
        self.assertEqual(True, q.is_cat_empty)
