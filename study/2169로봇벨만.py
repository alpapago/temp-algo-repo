import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = list()
for _ in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)

ans = 0

