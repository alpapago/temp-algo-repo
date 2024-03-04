import sys

sys.setrecursionlimit(10**6)

T = int(input())


def dfs(x):
    global cnt

    visited[x] = True
    cycle.append(x)
    next = num[x]
    if visited[next]:
        if next in cycle:
            cnt += len(cycle[cycle.index(next) :])
        return
    else:
        dfs(next)


for _ in range(T):
    n = int(input())

    num = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    visited[0] = True

    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - cnt)
