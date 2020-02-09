"""https://blog.csdn.net/xiangxianghehe/article/details/81805957"""
from unittest import TestCase
from .utils import *


def get_kth_num(bi_tree, k):
    """求二叉树第K层的节点个数"""
    if bi_tree is None or k < 1:
        return 0
    if k == 1:
        return 1
    left_num = get_kth_num(bi_tree.lchild, k-1)
    right_num = get_kth_num(bi_tree.rchild, k-1)
    return left_num + right_num


class Test(TestCase):

    def test_get_kth_num(self):
        datas = "ABCDEFGHIJ"
        bi_tree = gen_complete_bi_tree(datas)
        self.assertEqual(1, get_kth_num(bi_tree, 1))
        self.assertEqual(2, get_kth_num(bi_tree, 2))
        self.assertEqual(4, get_kth_num(bi_tree, 3))
        self.assertEqual(3, get_kth_num(bi_tree, 4))
        self.assertEqual(0, get_kth_num(bi_tree, 5))
        self.assertEqual(0, get_kth_num(bi_tree, 6))
        self.assertEqual(0, get_kth_num(bi_tree, 7))


