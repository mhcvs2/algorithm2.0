from unittest import TestCase


class Node(object):

    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        return self.data


def list_print(head):
    cur = head
    while cur is not None:
        print(cur.data, end="")
        if cur.next is not None:
            print(" -> ", end="")
        cur = cur.next
    print()


def reverse(head):
    if head is None or head.next is None:
        return head
    pre = head
    cur = head.next
    while cur is not None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    head.next = None
    return pre


class TestReverse(TestCase):

    def test_reverse1(self):
        head = Node(1, next_=Node(2, next_=Node(3, next_=Node(4))))
        list_print(head)
        list_print(reverse(head))
