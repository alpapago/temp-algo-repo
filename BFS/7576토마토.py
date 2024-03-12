from collections import deque

n, m = map(int, input().split())  # n:열, m:행
board = []
for _ in range(m):
    board.append(list(map(int, input().split())))


dist = [[0 for _ in range(n)] for _ in range(m)]
q = deque()
for i in range(m):
    for j in range(n):
        if board[i][j] > 0:
            q.append((i, j))
        elif board[i][j] == 0:
            dist[i][j] = -1


while q:
    r, c = q.popleft()
    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nr, nc = dr + r, dc + c

        if 0 > nr or nr >= m or 0 > nc or nc >= n:
            continue
        if dist[nr][nc] >= 0:
            continue
        dist[nr][nc] = dist[r][c] + 1
        q.append((nr, nc))

ans = 0
for r in range(m):
    for c in range(n):
        if dist[r][c] == -1:
            print(-1)
            exit(0)
        ans = max(ans, dist[r][c])

print(ans)
