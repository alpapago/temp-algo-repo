import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
belt = deque(list(map(int,input().split())))

# k개가 되면 break
isFull = k
ans = 0
robot = deque([0]*(n))

while True:
    
    ans += 1
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())

    if robot[n-1] == 1:
        robot[n-1] = 0
    # print(belt,'beforebelt')
    # print(robot,'beforerobot')
    if not robot[0]:
        if belt[0]:
            robot[0] = 1
            belt[0] -= 1
    else:
        if belt[1] and not robot[1]:
            robot[0] = 0
            robot[1] = 1
            belt[1] -= 1

    for i in range(n-2,0,-1):
        if belt[i+1] == 0:
            continue      
        # 이미 로봇 있으면 옮기기
        elif robot[i] and not robot[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1


    if robot[n-1] == 1:
        robot[n-1] = 0

    # print(robot,'afterrobot')
    # print(belt,'afterbelt')
    cnt = 0
    for i in belt:
        if i == 0:
            cnt += 1
    if cnt >= k:
        break
    # print(ans,'일때의 belt상태',belt)        
   

print(ans)