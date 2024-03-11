import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
pan = list()
visited = [[False for _ in range(m)] for _ in range(n)]
tot = list()

for _ in range(n):
    pan.append(list(map(int, input().split())))

for r in range(n):
    for c in range(m):
        if pan[r][c] == 1:
            tot.append([r, c])


def bfs(r, c):

    q = deque([r, c])
    visited[r][c] == 1

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_r = now_r + dr
            next_c = now_c + dc

            if 0 > next_r or next_r >= n or 0 > next_c or next_c >= m:
                continue

            if not visited[now_r][now_c]:
                visited[now_r][now_c] = True

                q.append([next_r, next_c])
