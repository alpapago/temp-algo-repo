import sys

input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(input().split()))

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for st in arr:
    print(st[0])
