n = int(input())

t = []
p = []
dp = [0] * (n + 1)
max_v = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    t.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_v)
        max_v = dp[i]

    else:
        dp[i] = max_v

print(max_v)
