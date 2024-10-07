import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
pan = list()
maxV = 0

for i in range(n):
    tmp = list(map(int, input().split(" ")))
    pan.append(tmp)
    for j in range(n):
        maxV = max(maxV, tmp[j])


def bfs(r, c, B, visit):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()

    q.append((r, c))
    # 방문 처리
    visit[r][c] = 1

    while q:
        nr, nc = q.popleft()
        for dr, dc in directions:
            new_r = nr + dr
            new_c = nc + dc
            if new_r < 0 or new_c < 0 or new_r >= n or new_c >= n:
                continue
            if visit[new_r][new_c]:
                continue
            if pan[new_r][new_c] <= B:
                continue
            visit[new_r][new_c] = 1
            q.append((new_r, new_c))


answer = 0
for b in range(maxV):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(n):
            if pan[r][c] > b and not visit[r][c]:
                bfs(r, c, b, visit)
                cnt += 1

    answer = max(answer, cnt)

print(answer)
