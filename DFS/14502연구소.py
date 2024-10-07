import sys

input = sys.stdin.readline

n, m = map(int, input().split())
co = [[0] * m for _ in range(n)]

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

result = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if co[i][j] == 0:
                score += 1
    return score


def virus(r, c):
    for dr, dc in dir:
        nr = r + dr
        nc = c + dc
        if 0 > nr or nr >= n or 0 > nc or nc >= m:
            continue
        if co[nr][nc] == 0:
            co[nr][nc] = 2
            virus(nr, nc)


def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                co[i][j] = arr[i][j]
        for i in range(n):
            for j in range(m):
                if co[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
                dfs(cnt)
                arr[i][j] = 0
                cnt -= 1


dfs(0)

print(result)
