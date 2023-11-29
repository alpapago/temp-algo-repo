n = 5
nums = [10,1,7,8,9]

def ans(n:int,nums:list[int]) -> list[int]:

    max_num = nums[-1]
    answer = [-1]
    stack = [nums.pop()]

    for i in range(n-2,-1,-1):
        tmp = nums[i]
        print(tmp)
        
        while stack and stack[-1] <= tmp:
            stack.pop()

        if not stack:
            answer.append(-1)
        else:
            answer.append(stack[-1])
     
        stack.append(tmp)
    return answer[::-1]

print(ans(n,nums))


''' 백준 제출용 코드 

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

max_num = nums[-1]
answer = [-1]
stack = [nums.pop()]

for i in range(n-2,-1,-1):
    tmp = nums[i]
    while stack and stack[-1] <= tmp:
        stack.pop()

    if not stack:
        answer.append(-1)
    else:
        answer.append(stack[-1])

    stack.append(tmp)

answer = answer[::-1]

for i in answer:
    print(i,end=' ')
'''