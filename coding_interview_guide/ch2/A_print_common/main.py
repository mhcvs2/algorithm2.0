import unittest


class Node(object):

    def __init__(self, value, n=None):
        self.value = value
        self.next = n


def print_common_part(h1, h2):
    print("common part: ")
    while h1 is not None and h2 is not None:
        if h1.value < h2.value:
            h1 = h1.next
        elif h2.value < h1.value:
            h2 = h2.next
        else:
            print(h1.value)
            h1 = h1.next
            h2 = h2.next


class TestPCP(unittest.TestCase):

    def testPCP(self):
        h1 = Node(1, Node(2, Node(3)))
        h2 = Node(1, Node(3, Node(5)))
        print_common_part(h1, h2)
