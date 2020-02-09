

class BiTree(object):

    def __init__(self, data=None, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.data = data


def gen_complete_bi_tree(datas):
    """ 生成完全二叉链表 """
    if len(datas) == 0:
        return None
    nodes = [BiTree(data=d) for d in datas]
    n = len(nodes)
    for i in range(n):
        if n > 2 * i + 1:
            nodes[i].lchild = nodes[2 * i + 1]
        if n > 2 * i + 2:
            nodes[i].rchild = nodes[2 * i + 2]
    return nodes[0]
