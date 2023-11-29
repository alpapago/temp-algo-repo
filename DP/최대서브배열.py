# 메모이제이션

def maxSubArray(nums: list[int]) -> int:
    for i in range(1,len(nums)):
        nums[i] += (nums[i-1] if nums[i-1] > 0 else 0)
    print(nums)
    return max(nums)
    
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# 카데인 알고리즘
import sys

def maxArray(nums:list[int]) -> int:
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum