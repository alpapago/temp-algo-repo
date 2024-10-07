import sys
input = sys.stdin.readline

n = int(input())
board = []

for r in range(n):
    tmp = list()
    t = input()
    for c in range(n):
        tmp.append(t[c])