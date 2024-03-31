import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
<<<<<<< HEAD
=======

>>>>>>> 02b5324d7e9036c8ab3463bcd6cfec8f191fe972
# 양분
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

<<<<<<< HEAD
# 나무에 나이별로 input
trees = [[] for _ in range(1011)]
for _ in range(m):
    x, y, age = map(int, input().split())
    trees[age].append([x - 1, y - 1, 0])
=======
trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)
>>>>>>> 02b5324d7e9036c8ab3463bcd6cfec8f191fe972

# 땅
pan = [[5 for _ in range(n)] for _ in range(n)]

while k:
    k -= 1
<<<<<<< HEAD
    # 초기화
    for age in range(1, 1011):
        if not trees[age]:
            continue
        # 나이가 age 나무에 대해서
        for tree in range(len(trees[age])):
            r, c, isUsed = trees[age][tree]
            if isUsed%2:
                trees[age][tree][2] += 1
    # 봄
    for age in range(1, 1011):
        if not trees[age]:
            continue
        # 나이가 age 나무에 대해서
        for tree in range(len(trees[age])):
            r, c, isUsed = trees[age][tree]
            if r<0  or c<0 or isUsed%2:
                continue
            if pan[r][c] >= age:
                # 나이만큼 양분먹고
                pan[r][c] -= age
                # 1살 더먹음
                trees[age + 1].append((r, c, isUsed+1))
                print(trees, "나이를 먹어야 하는데")
            else:
                # 여름에는 해당나무 죽어서 양분 됨
                yang = age // 2
                pan[r][c] += yang
            trees[age][tree] = [-1,-1, 0]
    print(trees, "after sprint")
    # 가을
    for age in range(1, 1011):
        if age % 5 != 0:
            continue
        for tree in trees[age]:
            r, c, isUsed = tree
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
                trees[1].append((nr, nc, 0))
=======
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
>>>>>>> 02b5324d7e9036c8ab3463bcd6cfec8f191fe972
    # 겨울
    for i in range(n):
        for j in range(n):
            pan[i][j] += arr[i][j]
    
<<<<<<< HEAD
    print(trees, "treeeeeeeeeeeeee")

# k년 지난 후 살아있는 나무 갯수
ans = 0
for age in range(1, 1011):
    if not trees[age]:
        continue
    for tree in range(len(trees[age])):
        if tree[]
        ans += len(trees[age])
=======
# k년 지난 후 살아있는 나무 갯수
ans = 0
for r in range(n):
    for c in range(n):
        tree = trees[r][c]
        if not tree:
            continue
        ans += len(tree)
>>>>>>> 02b5324d7e9036c8ab3463bcd6cfec8f191fe972
print(ans)
