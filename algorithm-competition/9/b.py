# 最多可嵌套矩形
# dp[i] = max{dp[j]+1 | (i, j)有边}
import copy

data = [(1, 1), (2, 2), (1, 5), (6, 2), (3, 4), (5, 6)]
n = 6

dp = [0 for _ in range(n)]
G = [[0 for _ in range(n)] for _ in range(n)]


def dfs(x):
    global data, n, dp, G
    if dp[x] > 0:
        return dp[x]
    for i in range(n):
        if G[x][i] > 0:
            dp[x] = max(dp[x], dfs(i)+1)
    return dp[x]


def print_ans(d, x):
    for i in range(n):
        if G[x][i] > 0 and d[x] == d[i] + 1:
            print(data[i], end=', ')
            print_ans(d, i)
            break


def solve():
    global data, n, dp, G
    for i in range(n):
        for j in range(n):
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                G[i][j] = 1
            if data[i][0] < data[j][1] and data[i][1] < data[j][0]:
                G[i][j] = 1
    # print(G)
    res = 0
    for i in range(n):
        dp = [0 for _ in range(n)]
        res = max(res, dfs(i))
        print_ans(dp, i)
        print()
    print(res)


if __name__ == '__main__':
    solve()

