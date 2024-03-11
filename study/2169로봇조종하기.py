from collections import deque

n, m = map(int, input().split())

board = list()
dp = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

dp[0][0] = board[0][0]

for r in range(n):
    if r != 1:
        left = [0 for _ in range(m)]
        right = [0 for _ in range(m)]
        left[0] = dp[r - 1][0] + board[r][0]
        right[0] = dp[r - 1][m - 1] + board[r][m - 1]

    for c in range(1, m):
        if r == 1:
            dp[r][c] = dp[r][c - 1] + board[r][c]
        else:
            left[c] = max(left[c - 1] + board[r][c], dp[r][c - 1] + board[r][c])

print(dp[n - 1][m - 1])
