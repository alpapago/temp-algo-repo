import sys
input = sys.stdin.readline

n = int(input())
board = []

for r in range(n):
    tmp = list(input().split())
    board.append(tmp)

visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
flag = False
for i in range(1,n):
    for j in range(1,n):
        if board[i][j] == 'S' or board[i][j] == 'T':
            if visited[i][j-1] == 0 or visited[i-1][j] == 0:
                flag = True
            if visited[i][j-1] == 1 or visited[i-1][j] == 1:
                flag = False
        if flag:
            visited[i][j] = 1

print(visited)