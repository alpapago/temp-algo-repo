n, m = map(int, input().split())

# 인접행렬
board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
print(board)

for i in range(m):
    a, b, c = map(int, input().split())
    board[a][b] = c
    board[b][a] = c
