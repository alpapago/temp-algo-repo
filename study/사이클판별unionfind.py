def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
num = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]

for i in range(1, n + 1):
    if find(parent, i) != find(parent, num[i]):
        union(parent, i, num[i])

print(parent, "parent")
