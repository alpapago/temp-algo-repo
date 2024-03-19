import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

# 양분
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

# 땅
pan = [[5 for _ in range(n)] for _ in range(n)]

while k:
    k -= 1
    # 봄
    for r in range(n):
        for c in range(n):
            tree = trees[r][c]
            idx = 0
            dead = []
            if not tree:
                continue
            tree.sort()
            for t in range(len(tree)):
                t_age = tree[t]
                if pan[r][c] >= t_age:
                    pan[r][c] -= t_age
                    trees[r][c][t] = t_age + 1
                else:
                    dead = tree[t:]
                    trees[r][c] = tree[:t]
                    break
            for d in dead:
                pan[r][c] += d//2          
            
    # 가을
    for r in range(n):
        for c in range(n):
            tree = trees[r][c]
            if not tree:
                continue
            for t in range(len(tree)):
                t_age = tree[t]
                if t_age%5 == 0:
                    for dr, dc in [
                        (-1, -1),
                        (-1, 0),
                        (-1, +1),
                        (0, -1),
                        (0, +1),
                        (+1, -1),
                        (+1, 0),
                        (+1, +1),
                    ]:
                        nr = r + dr
                        nc = c + dc
                        if 0 > nr or 0 > nc or nr >= n or nc >= n:
                            continue
                        trees[nr][nc].append(1)
    # 겨울
    for i in range(n):
        for j in range(n):
            pan[i][j] += arr[i][j]
    
# k년 지난 후 살아있는 나무 갯수
ans = 0
for r in range(n):
    for c in range(n):
        tree = trees[r][c]
        if not tree:
            continue
        ans += len(tree)
print(ans)
