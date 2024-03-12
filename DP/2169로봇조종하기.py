n, m = map(int, input().split())

board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = board[0][0]

for r in range(n):
    if r == 0:
        for c in range(1, m):
            dp[r][c] = dp[r][c - 1] + board[r][c]
    else:
        toright = board[r][:]
        toleft = board[r][:]
        toright[0] = board[r][0]
        toleft[m - 1] = board[r][m - 1]
        for c in range(1, m):
            toright[c] = toright[c - 1] + toright[c]
        for c in range(m - 2, 0):
            toleft[c] = toleft[c + 1] + toleft[c]

    print(toleft, "left")
    print(toright, "toright")
    for i in range(m):
        dp[r][i] = max(toright[i], toleft[i])

print(dp[n - 1][m - 1])
