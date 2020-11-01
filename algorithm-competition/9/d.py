# 0-1背包问题
# dp[i][j] = max{dp[i+1][j], dp[i+1][j-v[i]]+1}

# 体积
v = [4, 2, 1, 5]
# 重量
w = [1, 2, 3, 4]
C = 10
n = 4

dp = [[0 for _ in range(C+1)] for i in range(n+1)]


def solve():
    for i in range(n-1, -1, -1):
        for j in range(C+1):
            dp[i][j] = 0 if i == n-1 else dp[i+1][j]
            if j >= v[i]:
                dp[i][j] = max(dp[i][j], dp[i+1][j-v[i]]+w[i])
    return dp[0][C]


if __name__ == '__main__':
    print(solve())
