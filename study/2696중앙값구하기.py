import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m = int(input())
    nums = list()

    for _ in range(m//10+1):
        nums.extend(list(map(int,input().split())))

    ans = [nums[0]]
    now = nums[0]
    left = []
    right = []
    for i in range(1,m):
        tmp = nums[i]
        
        if tmp < now:
            heapq.heappush(left,-tmp)
        else:
            heapq.heappush(right,tmp)

        # 홀수번째일때
        if i%2 == 0:
            if len(left) > len(right):
                heapq.heappush(right,now)
                now = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left,-now)
                now = heapq.heappop(right)
            ans.append(now)
    print(len(ans))
    for i in range(len(ans)):
        if i%10 == 9:
            print(ans[i], end='\n')
        else:
            print(ans[i],end=' ')
    ans = []