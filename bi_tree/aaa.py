# encoding: utf-8
from bi_tree.lib.utils import *


def default_handler(node):
    print(node.data, end=' ')


def pre_order_traverse(bi_tree, handler=default_handler):
    if bi_tree is None:
        return
    handler(bi_tree)
    pre_order_traverse(bi_tree.lchild, handler)
    pre_order_traverse(bi_tree.rchild, handler)


def in_order_traverse(bi_tree, handler=default_handler):
    if bi_tree is None:
        return
    in_order_traverse(bi_tree.lchild, handler)
    handler(bi_tree)
    in_order_traverse(bi_tree.rchild, handler)


def post_order_traverse(bi_tree, handler=default_handler):
    if bi_tree is None:
        return
    post_order_traverse(bi_tree.lchild, handler)
    post_order_traverse(bi_tree.rchild, handler)
    handler(bi_tree)


# bfs
def level_traverse(bi_tree, handler=default_handler):
    queues = list()
    queues.append(bi_tree)
    while len(queues) > 0:
        node = queues.pop(0)
        handler(node)
        if node.lchild:
            queues.append(node.lchild)
        if node.rchild:
            queues.append(node.rchild)


def t1():
    datas = "ABCDEFGHIJ"
    bi_tree = gen_complete_bi_tree(datas)

    pre_order_traverse(bi_tree)
    # A B D H I E J C F G
    print()

    in_order_traverse(bi_tree)
    # H D I B J E A F C G
    print()

    post_order_traverse(bi_tree)
    # H I D J E B F G C A
    print()

    level_traverse(bi_tree)
    # A B C D E F G H I J
    print()


if __name__ == '__main__':
    t1()
