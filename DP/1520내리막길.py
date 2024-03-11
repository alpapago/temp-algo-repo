import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1


def dp1(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0

    else:
        dp[x][y] = 0

    if 0 <= x - 1 < m and 0 <= y - 1 < n:
        dp[x][y] += max(dp1(x - 1, y), dp1(x + 1, y), dp1(x, y - 1), dp1(x, y + 1))

    return dp[x][y]


dp1(0, 0)
print("111111")
print(dp)
print(dp[n - 1][m - 1])
