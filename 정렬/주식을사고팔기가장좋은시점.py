import sys
nums = [7,1,5,3,6,4]

def time(nums:list[int])->int:
    min_price = sys.maxsize
    profit = 0

    for num in nums:
        min_price = min(min_price,num)
        profit = max(profit,num-min_price)

    return profit

print(time(nums))