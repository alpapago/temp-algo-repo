nums = [0,1,0,2,1,0,1,3,2,1,2,1]

# 투포인터로 풀기
def trap(height:list[int])->int:
    if not height:
        return 0
    
    volumn = 0
    left,right = 0,len(height)-1
    left_max, right_max = height[left],height[right]

    while left < right :
        left_max,right_max = max(height[left],left_max), max(height[right],right_max)

        # max값 중에서는 작은거 취하기
        if left_max <= right_max:
            volumn += left_max - height[left]
            left += 1
        else:
            volumn += right_max - height[right]
            right -= 1
    
    return volumn

print(trap(nums))

# 스택써서 풀기
def trap_stack(height:list[int]) -> int:
    stack = []
    volumn = 0

    for i in range(len(height)):
        
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            # 스택이 비어있으면 break
            if not stack:
                break
            
            # 이전과의 차이만큼 물 처리?
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]-height[top])
            volumn += distance*waters 


        # 값 하나 추가
        stack.append(i)
    return volumn