nums = [2,7,11,15]
target = 9

# in 구현
def twoSum(nums:list[int], target:int) -> list[int]:
    for i,n in enumerate(nums):
        new = target - n
        if new in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(new) + i + 1]

print(twoSum(nums,target))

# key-value
def two(nums:list[int],target:int)->int:
    num_map = dict()

    for i, num in enumerate(nums):
        num_map[num] = i
    
    for i, num in enumerate(nums):
        if target - num in num_map and i != num_map[target-num]:
            return [num_map[target-num], i]

print(two(nums,target))

# key value 개선
def fix_two(nums:list[int],target:int)->int:
    num_map = dict()

    for i, num in enumerate(nums):
        # 정답에 해당하면 return 먼저!
        if target - num in num_map:
            return [i, num_map[target-num]]
        
        # 아니라면...
        num_map[num] = i

print(fix_two(nums,target))
