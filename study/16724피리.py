import sys

sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(input())


def move(s, r, c):
    if s == "U":
        return r - 1, c
    elif s == "D":
        return r + 1, c
    elif s == "L":
        return r, c - 1
    else:
        return r, c + 1


def dfs(nr, nc):
    global ans
    visited[nr][nc] = True
    cycle.append((nr, nc))

    x, y = move(board[nr][nc], nr, nc)

    if 0 <= x < r and 0 <= y < c:
        if visited[x][y]:
            if (x, y) in cycle:
                ans += 1
            return

        else:
            dfs(x, y)


visited = [[False] * c for _ in range(r)]
ans = 0

for now_r in range(r):
    for now_c in range(c):
        if not visited[now_r][now_c]:
            cycle = []
            dfs(now_r, now_c)

print(ans)
