from collections import deque
import copy

n = int(input())

pan = list()

for _ in range(n):
    tmp = input()
    t = []
    for i in range(n):
        t.append(tmp[i])
    pan.append(t)

red = copy.deepcopy(pan)
v_1 = [[0 for _ in range(n)] for _ in range(n)]
v_2 = [[0 for _ in range(n)] for _ in range(n)]


def bfs(r, c, visited, p):
    visited[r][c] = 1
    q = deque()

    q.append((r, c))

    while q:
        n_r, n_c = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_r = n_r + dr
            new_c = n_c + dc
            if 0 > new_r or 0 > new_c or new_r >= n or new_c >= n:
                continue
            if visited[new_r][new_c]:
                continue
            if p[n_r][n_c] == p[new_r][new_c]:
                q.append((new_r, new_c))
                visited[new_r][new_c] = 1


ans1 = 0
for r in range(n):
    for c in range(n):
        if not v_1[r][c]:
            bfs(r, c, v_1, pan)
            ans1 += 1

for r in range(n):
    for c in range(n):
        if red[r][c] == "G":
            red[r][c] = "R"

ans2 = 0

for r in range(n):
    for c in range(n):
        if not v_2[r][c]:
            bfs(r, c, v_2, red)
            ans2 += 1

print(ans1, ans2)
