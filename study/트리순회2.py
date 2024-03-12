import sys

sys.setrecursionlimit(10**6)

n = int(input())
tree = dict()

for _ in range(n):
    a, b, c = map(int, input().split(" "))
    tree[a] = [b, c]

visited = []
ans = []
pre = []
mid = []
cnt = 0


def dfs(v):
    global cnt
    visited.append(v)
    cnt += 1
    print(v, "11")
    # leaf node
    if tree[v][0] == -1 and tree[v][1] == -1:
        if len(visited) != n:

            # cnt += 1
            return

    if tree[v][0] != -1:

        cnt += 1
        dfs(tree[v][0])
        print(v, "333")

    if tree[v][1] != -1:
        cnt += 1

        dfs(tree[v][1])
        print(v, "444")

    print(v, "222")


dfs(1)
# print(ans)

print(cnt + 1)
