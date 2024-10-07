from collections import deque
import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]

result = 0

###### 진행중...
