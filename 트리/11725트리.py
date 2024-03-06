import sys

sys.setrecursionlimit(10**6)

n = int(input())

data = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

parent = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]


def dfs(v, parent, visited):
    if visited[v]:
        return

    visited[v] = 1

    for i in data[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i, parent, visited)


dfs(1, parent, visited)

for i in range(2, n + 1):
    print(parent[i])
