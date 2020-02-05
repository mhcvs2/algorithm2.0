# encoding: utf-8


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


def default_handler(node):
    print(node.data, end=' ')


def pre_order_traverse(bi_tree, handler=default_handler):
    if bi_tree is None:
        return
    handler(bi_tree)
    pre_order_traverse(bi_tree.lchild)
    pre_order_traverse(bi_tree.rchild)


def in_order_traverse(bi_tree, handler=default_handler):
    if bi_tree is None:
        return
    in_order_traverse(bi_tree.lchild)
    handler(bi_tree)
    in_order_traverse(bi_tree.rchild)


def post_order_traverse(bi_tree, handler=default_handler):
    if bi_tree is None:
        return
    post_order_traverse(bi_tree.lchild)
    post_order_traverse(bi_tree.rchild)
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
