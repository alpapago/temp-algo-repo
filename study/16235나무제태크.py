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
    trees[age].append([x - 1, y - 1, 0])

# 땅
pan = [[5 for _ in range(n)] for _ in range(n)]

while k:
    k -= 1

    # 봄
    for age in range(len(trees)):
        for tree in range(len(trees[age])):
            r, c, isUsed = trees[age]
            isUsed = isUsed%2
            if r < 0 or c < 0:
                continue
            if pan[r][c] >= age and not isUsed:
                pan[r][c] -= age
                # 1살 더먹음
                trees[age + 1].append([r, c, isUsed+1])
                # print(trees, "나이를 먹어야 하는데")
            else:
                # 여름에는 해당나무 죽어서 양분 됨
                pan[r][c] += age//2
            # print(trees, "빠지기 전")
            trees[i][1] = -1
            trees[i][2] = -1
            # print(trees, "잘빠지고있는건가")
    # print(trees, "after sprint")
    # 가을
    for i in range(len(trees)):
        age, r, c = trees[i]
        if not age % 5 and r >= 0 and c >= 0:
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
                trees.append([1, nr, nc])
    # 새 나무 추가되고 sort
    trees = sorted(trees, key=lambda x: x[0])
    # 겨울
    for i in range(n):
        for j in range(n):
            pan[i][j] += arr[i][j]
    # print(trees, "treeeeeeeeeeeeee")

# k년 지난 후 살아있는 나무 갯수
ans = 0
for i in range(len(trees)):
    age, r, c = trees[i]
    if r >= 0 and c >= 0:
        ans += 1
print(ans)
