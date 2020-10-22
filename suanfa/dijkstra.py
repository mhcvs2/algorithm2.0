import sys


link_list = []
max_id = 5


class Edge(object):

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w


class Record(object):

    def __init__(self, id, dist=sys.maxsize):
        self.id = id
        self.dist = dist


def add_edge(x, y, w):
    global link_list
    link_list[x].append(Edge(x, y, w))


def load():
    global link_list
    link_list = [[] for _ in range(max_id+1)]
    add_edge(0, 1, 10)
    add_edge(0, 4, 15)
    add_edge(1, 2, 15)
    add_edge(1, 3, 2)
    add_edge(2, 3, 1)
    add_edge(2, 5, 5)
    add_edge(3, 5, 12)
    add_edge(4, 5, 10)
    book = [False] * max_id
    processor = [-1] * 100



def solve(s, t):
    pass


if __name__ == '__main__':
    load()
    print(solve(0, 5))
