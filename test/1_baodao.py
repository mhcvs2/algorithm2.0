# encoding: utf-8
"""
10 10 6 8
1 2 1 0 0 0 0 0 2 3
3 0 2 0 1 2 1 0 1 2
4 0 1 0 1 2 3 2 0 1
3 2 0 0 0 1 2 4 0 0
0 0 0 0 0 0 1 5 3 0
0 1 2 1 0 1 5 4 3 0
0 1 2 3 1 3 6 2 1 0
0 0 3 4 8 9 7 5 0 0
0 0 0 3 7 8 6 0 1 2
0 0 0 0 0 0 0 0 1 0

宝岛探险
m*n 格子
0代表海洋，1-9 都是陆地，数字是海拔
p，q 是起点
"""

m = 10
n = 10
p = 6
q = 8
data = [
    [1, 2, 1, 0, 0, 0, 0, 0, 2, 3],
    [3, 0, 2, 0, 1, 2, 1, 0, 1, 2],
    [4, 0, 1, 0, 1, 2, 3, 2, 0, 1],
    [3, 2, 0, 0, 0, 1, 2, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 5, 3, 0],
    [0, 1, 2, 1, 0, 1, 5, 4, 3, 0],
    [0, 1, 2, 3, 1, 3, 6, 2, 1, 0],
    [0, 0, 3, 4, 8, 9, 7, 5, 0, 0],
    [0, 0, 0, 3, 7, 8, 6, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

next_ = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


def print_(d):
    for i in range(m):
        for j in range(n):
            print(d[i][j], end=' ')
        print()


# bfs求岛面积
def bfs():
    book = [[0 for _ in range(n)] for _ in range(m)]
    que = [(p, q)]
    book[p][q] = 1
    area = 1
    while len(que) > 0:
        cur = que.pop(0)
        # print(cur)
        for i in range(4):
            nx = cur[0] + next_[i][0]
            ny = cur[1] + next_[i][1]
            if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                continue
            if data[nx][ny] > 0 and book[nx][ny] == 0:
                book[nx][ny] = 1
                que.append((nx, ny))
                area += 1
    return area
# 38


dfs_area = 0


def dfs(cur, book):
    global dfs_area
    for i in range(4):
        nx = cur[0] + next_[i][0]
        ny = cur[1] + next_[i][1]
        if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
            continue
        if data[nx][ny] > 0 and book[nx][ny] == 0:
            book[nx][ny] = 1
            dfs_area += 1
            dfs((nx, ny), book)


def dfs_solve():
    cur = (p, q)
    global dfs_area
    dfs_area = 1
    book = [[0 for _ in range(n)] for _ in range(m)]
    book[p][q] = 1
    dfs(cur, book)
    return dfs_area
# 38


# 求有几个小岛
def dfs_color(cur, book, color):
    data[cur[0]][cur[1]] = color
    for i in range(4):
        nx = cur[0] + next_[i][0]
        ny = cur[1] + next_[i][1]
        if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
            continue
        if data[nx][ny] > 0 and book[nx][ny] == 0:
            book[nx][ny] = 1
            dfs_color((nx, ny), book, color)


def dfs_color_solve():
    color = 0
    book = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            book[i][j] = 1
            if data[i][j] > 0:
                color -= 1
                dfs_color((i, j), book, color)
                # print("------------------------")
                # print_(data)
    return -1 * color
# 4


if __name__ == '__main__':
    print(dfs_color_solve())
