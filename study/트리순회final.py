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


def dfs1(v):
    global cnt
    if v == -1:
        return
    cnt += 1
    dfs1(tree[v][1])


dfs1(1)
print(2 * (n - 1) - cnt + 1)
