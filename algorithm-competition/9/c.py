# n种面值硬币，每种都有无限多个, 取和为S的，最多或最少
# dp[S] = max{dp[S-data[i]]+1 | i属于{0~n}}

data = [1, 5, 10, 20, 50, 100]
n = 6
S = 420
dp = [-1 for _ in range(S+1)]
dp2 = [float("inf") for _ in range(S+1)]


def dfs(x):
    global data, n, S, dp, dp2
    if dp[x] >= 0:
        return dp[x]
    for i in range(n):
        if x >= data[i]:
            dp[x] = max(dp[x], dfs(x-data[i]) + 1)
    return dp[x]


def dfs_min(x):
    global data, n, S, dp, dp2
    if dp2[x] < float("inf"):
        return dp2[x]
    # print(x)
    for i in range(n):
        if x >= data[i]:
            dp2[x] = min(dp2[x], dfs_min(x-data[i]) + 1)
    return dp2[x]


def print_ans(d, x):
    global data, n, S, dp, dp2
    for i in range(n):
        if x >= data[i] and d[x] == d[x-data[i]] + 1:
            print(data[i], end=", ")
            print_ans(d, x-data[i])
            break


def solve():
    global data, n, S, dp, dp2
    dp[0] = 0
    dp2[0] = 0
    # print(dfs(S))
    # print_ans(dp, S)
    print(dfs_min(S))
    print_ans(dp2, S)


if __name__ == '__main__':
    solve()
