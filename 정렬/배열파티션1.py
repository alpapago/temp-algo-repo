nums = [1,4,3,2]

def part(nums:list[int])-> int:
    return sum(sorted(nums[::2]))

print(part(nums))