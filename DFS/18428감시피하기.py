import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

teacher = []
space = []

board = []

for r in range(n):
    tmp = list(input().split())
    board.append(tmp)
    for c in range(n):
        if tmp[c] == "T":
            teacher.append((r, c))
        if tmp[c] == "X":
            space.append((r, c))


def check(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x += 1
    return False


def process():
    for x, y in teacher:
        for i in range(4):
            if check(x, y, i):
                return True
    return False


find = False

for data in combinations(space, 3):
    for x, y in data:
        board[x][y] = "O"
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = "X"

if find:
    print("YES")
else:
    print("NO")
