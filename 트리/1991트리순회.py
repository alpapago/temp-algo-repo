import copy

n = int(input())
node = dict()
visited = dict()

for _ in range(n):
    p, a, b = input().split(" ")
    node[p] = [a, b]
    visited[p] = 0
preans = []
midans = []
postand = []
v1 = copy.deepcopy(visited)
v2 = copy.deepcopy(visited)
v3 = copy.deepcopy(visited)


def pre(v):
    if v == ".":
        return
    if not v1[v]:
        v1[v] = 1
        preans.append(v)

        pre(node[v][0])
        pre(node[v][1])


pre("A")

print("".join(preans))

visited = dict()


def mid(v):
    if v == ".":
        return
    if not v2[v]:
        v2[v] = 1
        mid(node[v][0])
        midans.append(v)
        mid(node[v][1])


mid("A")
print("".join(midans))


def post(v):
    if v == ".":
        return
    if not v3[v]:
        v3[v] = 1
        post(node[v][0])
        post(node[v][1])
        postand.append(v)


post("A")
print("".join(postand))
