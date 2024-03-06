n = int(input())

tree = [(0, 0)]
for _ in range(n):
    t, l, r = map(int, input().split())
    tree.append((l, r))

ans = list()
stack = list()
flag = True
visit = list()
last = 0


def dfs(node, parent, w):
    global stack, n, visit, flag

    if node != -1:
        stack.append(node)

    if node == -1:
        if w == 1:
            flag = False
        return
    visit.append(node)
    print(visit, "visit")

    if len(visit) == n:
        flag = False
    dfs(tree[node][0], node, 0)
    if stack[-1] != node:
        if flag:
            stack.append(node)
    dfs(tree[node][1], node, 1)
    if stack[-1] != node:
        if flag:
            stack.append(node)


dfs(1, 1, 0)
print(stack, "stack")


if len(stack):
    print(len(stack) - 1)
else:
    print(0)
