from collections import deque

n = int(input())
m = int(input())

# 0 : 빨간색 보도블록
# 1 : 회색 보도블록
board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

# 점프력 x
x = int(input())


def make_manhatan(dist):
    directions = list()

    x = dist
    y = 0
    while x >= 0:
        directions.append((x, y))
        x -= 1
        y += 1
    return directions


direction = make_manhatan(x)

q = deque([[0, 0]])

flag = False
jr = 0
jc = 0

while jr <= n - 1 and jc <= m - 1:
    if len(q) == 0:
        break

    jr, jc = q.popleft()

    if jr == n - 1 and jc == m - 1:
        flag = True
        break

    for dr, dc in direction:
        nr = jr + dr
        nc = jc + dc
        if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1:
            continue
        if board[nr][nc] == board[jr][jc]:
            q.append((nr, nc))

if flag == True:
    print("ALIVE")
else:
    print("DEAD")
