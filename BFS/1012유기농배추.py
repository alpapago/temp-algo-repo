from collections import deque

T = int(input())


def bfs(ir, ic):
    q = deque()
    q.append((ir, ic))
    pan[ir][ic] = 0

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_r, new_c = now_r + dr, now_c + dc
            if 0 > new_r or new_r >= n or 0 > new_c or new_c >= m:
                continue
            if pan[new_r][new_c] == 1:
                pan[new_r][new_c] = 0
                q.append((new_r, new_c))
    return 1


for _ in range(T):
    m, n, k = map(int, input().split())
    pan = [[-1 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        c, r = map(int, input().split())
        pan[r][c] = 1

    ans = 0
    for r in range(n):
        for c in range(m):
            if pan[r][c] == 1:
                ans += bfs(r, c)

    print(ans)
