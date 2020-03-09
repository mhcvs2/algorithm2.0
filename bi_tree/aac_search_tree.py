from .lib.utils import *
from .lib.base import BiTreeTestBase


def inert_bst(node, to_insert_data):
    if node is None:
        node = Node(to_insert_data)
    elif node.data > to_insert_data:
        node.l = inert_bst(node.l, to_insert_data)
    elif node.data < to_insert_data:
        node.r = inert_bst(node.r, to_insert_data)
    return node


def gen_bst(datas):
    if datas is None or len(datas) == 0:
        return None
    bst = None
    for i in range(len(datas)):
        bst = inert_bst(bst, datas[i])
    return bst


class BSTTest(BiTreeTestBase):

    def test_gen_bst(self):
        datas = [61, 87, 59, 47, 35, 73, 51, 98, 37, 93, 60]
        bst = gen_bst(datas)
        self.validate(bst,
                      pre_order=[61, 59, 47, 35, 37, 51, 60, 87, 73, 98, 93],
                      level=[61, 59, 87, 47, 60, 73, 98, 35, 51, 93, 37])
