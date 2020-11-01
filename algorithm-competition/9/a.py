

data = [
    [1, 0, 0, 0],
    [3, 2, 0, 0],
    [4, 10, 1, 0],
    [4, 3, 2, 20]
]

backtrack_max_sum = 0
m = n = 4


class Node(object):

    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        return str(self.data)


root_node = Node((-1, -1))


from functools import wraps
import time


def timefn(fn):
    """计算性能的修饰器"""
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1: .5f} s")
        return result
    return measure_time


def _print_node(node):
    first = True
    while node is not None:
        if first:
            first = False
        else:
            print('->', end=' ')
        print(node, end=' ')
        node = node.next
    print()


def backtrack(x, y, sum_):
    global backtrack_max_sum, m, n
    sum_ += data[x][y]
    if x == m-1:
        if backtrack_max_sum < sum_:
            backtrack_max_sum = sum_
        return
    backtrack(x+1, y, sum_)
    backtrack(x+1, y+1, sum_)


def backtrack2(x, y, sum_, node):
    global backtrack_max_sum, m, n, root_node
    sum_ += data[x][y]
    node.next = Node((x, y))
    if x == m-1:
        _print_node(root_node.next)
        if backtrack_max_sum < sum_:
            backtrack_max_sum = sum_
        return
    backtrack2(x+1, y, sum_, node.next)
    if node.next.next:
        node.next.next = None
    backtrack2(x+1, y+1, sum_, node.next)


def dfs(x, y):
    if x == m - 1:
        sum_ = 0
    else:
        sum_ = max(dfs(x+1, y), dfs(x+1, y+1))
    return data[x][y] + sum_


book = [[-1 for _ in range(n)] for _ in range(m)]


def dfs2(x, y):
    if x == m -1:
        sum_ = 0
    else:
        left = book[x+1][y] if book[x+1][y] > -1 else dfs2(x + 1, y)
        right = book[x+1][y+1] if book[x+1][y+1] > -1 else dfs2(x + 1, y+1)
        sum_ = max(left, right)
    res = data[x][y] + sum_
    book[x][y] = res
    return res


def solve():
    for i in range(n):
        book[n-1][i] = data[n-1][i]
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            book[i][j] = data[i][j] + max(book[i+1][j], book[i+1][j+1])
    print(book[0][0])


if __name__ == '__main__':
    # backtrack2(0, 0, 0, root_node)
    # print(backtrack_max_sum)
    # print(dfs2(0, 0))
    solve()
