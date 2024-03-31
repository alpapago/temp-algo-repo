import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

nums.sort()

for i in range(m):
    target = targets[i]

    start = 0 
    end = n-1

    mid = (start + end)//2
    while start <= end:
        if target < nums[mid]:
