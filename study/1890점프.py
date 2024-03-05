n = int(input())

pan = list()
dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    pan.append(list(map(int, input().split())))

dp[0][0] = 1

for r in range(n):
    for c in range(n):
        new_r = r + pan[r][c]
        new_c = c + pan[r][c]
        if r == n - 1 and c == n - 1:
            print(dp[n - 1][n - 1])
            exit(0)
        if new_r < n:
            dp[new_r][c] += dp[r][c]

        if new_c < n:
            dp[r][new_c] += dp[r][c]
