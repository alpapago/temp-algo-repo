import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))
woods = list(map(int, input().split(" ")))

# 이진 탐색을 위해서는 sort필요
woods.sort()
start, end = 0, n - 1
mid = (start + end) // 2

while woods[start] <= woods[end]:
    tree = 0

    for wood in woods:
        if wood > woods[mid]:
            tree += wood - woods[mid]

    if tree >= m:
        mid += 1


print(end)
