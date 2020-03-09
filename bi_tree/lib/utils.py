from unittest import TestCase


class Node(object):

    def __init__(self, data=None, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.data = data

    @property
    def l(self):
        return self.lchild

    @l.setter
    def l(self, data):
        self.lchild = data

    @property
    def r(self):
        return self.rchild

    @r.setter
    def r(self, data):
        self.rchild = data


def gen_complete_bi_tree(datas):
    """ 生成完全二叉链表 """
    if len(datas) == 0:
        return None
    nodes = [Node(data=d) for d in datas]
    n = len(nodes)
    for i in range(n):
        if n > 2 * i + 1:
            nodes[i].lchild = nodes[2 * i + 1]
        if n > 2 * i + 2:
            nodes[i].rchild = nodes[2 * i + 2]
    return nodes[0]


def print_red(msg):
    print("\033[0;31;40m\t%s\033[0m" % str(msg))


def print_blue(msg):
    print("\033[0;34;40m\t%s\033[0m" % str(msg))
