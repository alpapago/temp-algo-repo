n = int(input())
data = [[] for _ in range(n + 1)]

for _ in range(n):
    n, a, b = map(int, input().split(" "))
    data[n].append(a)
    data[n].append(b)

visited = [0 for _ in range(n + 1)]
ans = []
pre = []
last = 0


def dfs(v):
    global last

    if v == -1:
        return

    if not visited[v]:
        visited[v] = 1
        pre.append(v)
        if len(pre) == n:
            last = v
        ans.append(v)
        dfs(data[v][0])
        if ans[-1] == last:
            return
        if ans[-1] != v:
            ans.append(v)
        dfs(data[v][1])
        if ans[-1] == last:
            return
        if ans[-1] != v:
            ans.append(v)


dfs(1)
print(ans, "ans")

if ans:
    print(len(ans) - 1)
else:
    print(0)
