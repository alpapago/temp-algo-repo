from collections import deque

c, r = map(int, input().split())
fire = deque()

dist = [[0 for _ in range(c)] for _ in range(r)]
jihun = (0, 0)

for i in range(r):
    tmp = input()
    for j in range(c):
        if tmp[j] == "*":
            fire.append([i, j])
        elif tmp[j] == ".":
            dist[i][j] = -1
        elif tmp[j] == "@":
            jihun = (i, j)
        elif tmp[j] == "#":
            dist[i][j] = -2

for i in fire:
    i.append(jihun[0])
    i.append(jihun[1])

print(fire, "fire")
print(dist, "dist")


flag = False

while fire:
    now_r, now_c, jr, jc = fire.popleft()
    print(now_r, now_c, "now_rnow_c")
    if jr == r - 1 or jc == c - 1:
        print(dist[jr][jc] + 1)
        flag = True
        break

    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nr, nc = now_r + dr, now_c + dc
        print(nr, nc, "nrnc")
        njr, njc = jr + dr, jc + dc
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

        # 불이안번져
        if dist[nr][nc] == -2:
            continue
        # # 이동할 수 있는경우
        # if dist[njr][njc] == -1:
        #     dist[njr][njc] = dist[jr][jc] + 1
        #     fire.append((now_r, now_c, njr, njc))
        #     print(dist, "111")
        # else:
        # 불 붙여
        dist[nr][nc] = 0
        # 이동하려는 곳에 불이 안붙었다
        if dist[njr][njc] == -1:
            # 이동
            dist[njr][njc] = dist[jr][jc] + 1
            fire.append((nr, nc, njr, njc))
            print("2222222")

if flag:
    exit(0)
else:
    print("IMPOSSIBLE")
