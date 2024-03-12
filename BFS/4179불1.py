from collections import deque

r, c = map(int, input().split())
pan = list()
q = deque()

dist = [[0 for _ in range(c)] for _ in range(r)]
jihun = (0, 0)
for i in range(r):
    pan.append(input().split())
    for j in range(c):
        if pan[j] == "F":
            q.append((i, j))
        elif pan[j] == ".":
            dist[i][j] = -1
        elif pan[j] == "J":
            jihun = (i, j)

# q: 불이 번짐 and 지훈이 이동
flag = False
while q:
    now_r, now_c = q.popleft()
    jr, jc = jihun
    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nr, nc = now_r + dr, now_c + dc
        nj, nc = jr + dr, jc + dc
        if (
            0 > nr
            or 0 > nc
            or 0 > jr
            or 0 > jc
            or nr >= r
            or nc >= c
            or jr >= r
            or jc >= c
        ):
            continue
        if dist[nr][nc] > 0:
            continue
        if pan[nr][nc] == "#" or pan[jr][jc] == "#":
            continue
        if jr == r or jc == c:
            flag = True
            break
        dist[nr][nc] = dist[now_r][now_c] + 1
    if flag:
        break

if flag:
    ans = 0
    for i in range(r):
        for j in range(c):
            ans = max(dist[i][j] + 1, ans)

    print(ans)
else:
    print("IMPOSSIBLE")
