import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

ans = -1
start = 0
end = n - m + 1

ans_list = []
while start <= end:
    mid = end - 1
    while sum(nums[start:mid]) > sum(nums[mid:end]):
        mid -= 1
        if sum(nums[start:mid]) < sum(nums[mid:end]):
            start = mid
            ans_list.append(sum(nums[start:mid]))

print(max(ans_list))
