from collections import deque

n, k = map(int, input().split())
arr = []
q = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] != 0:
            q.append((arr[i][j], 0, i, j))

s, x, y = map(int, input().split())

q.sort(key=lambda x: x[0])

q = deque(q)
while q:
    now_v, now_t, r, c = q.popleft()
    if now_t == s:
        break
    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if 0 > nr or 0 > nc or n <= nr or n <= nc:
            continue
        if arr[nr][nc] != 0:
            continue
        if arr[nr][nc] == 0:
            arr[nr][nc] = now_v
            q.append((now_v, now_t + 1, nr, nc))

print(arr[x - 1][y - 1])
