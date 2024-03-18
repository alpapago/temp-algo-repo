import sys

input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))

stack = [board[0]]
ans = [0 for _ in range(n)]

for i in range(1, n):
    if stack[-1] > board[i]:
        ans[i] = stack[-1]
        stack.append(board[i])
        continue
    while stack[-1] < board[i]:
        stack.pop()
    if not stack:
        stack.append(board[i])
    else:
        ans[i] = stack[-1]
        stack.append(board[i])

for i in range(n):
    print(ans[i], end=" ")
