import unittest
from ch2.base import BaseUtils
from ch2.test import TestSingle


def delete_middle(head):
    l = BaseUtils.get_length(head)
    if l in (0, 1):
        return head
    if l == 2:
        return head.next
    to_delete_index = int((l-1) / 2)
    cur = head
    while to_delete_index > 1:
        cur = cur.next
        to_delete_index -= 1
    cur.next = cur.next.next
    return head


def delete_middle_book(head):
    if head is None or head.next is None:
        return head
    if head.next.next is None:
        return head.next
    pre = head
    cur = head.next.next
    while cur.next is not None and cur.next.next is not None:
        pre = pre.next
        cur = cur.next.next
    pre.next = pre.next.next
    return head


class TestDeleteMiddle(TestSingle):

    def test_delete_middle(self):
        print('test_delete_middle-----------------')
        self.print_datas()
        print('---------------------')
        for i in range(len(self.datas)):
            self.datas[i] = delete_middle(self.datas[i])
        self.print_datas()

    def test_delete_middle_book(self):
        print('test_delete_middle_book-----------------')
        self.print_datas()
        print('---------------------')
        for i in range(len(self.datas)):
            self.datas[i] = delete_middle_book(self.datas[i])
        self.print_datas()


if __name__ == '__main__':
    unittest.main()
