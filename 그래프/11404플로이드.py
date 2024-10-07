INF = int(1e9)

n = int(input())

m = int(input())

arr = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            arr[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < arr[a][b]:
        arr[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if arr[a][b] == INF:
            print(0, end=" ")
        else:
            print(arr[a][b], end=" ")
    print()
