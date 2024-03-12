from collections import deque

topni = []

for _ in range(4):
    tmp = deque([])
    tmp_input = input()
    for i in range(len(tmp_input)):
        tmp.append(tmp_input[i])
    topni.append(tmp)

# 한쪽 방향으로만 탐색하게 되니까 함수를 방향마다 재귀로 탐색
def toleft(num, t):
    
    if num < 0:
        return
    
    if topni[num+1][6] != topni[num][2]:
        move[num] = t
        toleft(num-1,-1*t)
    
    

def toright(num, t):
  
    if num > 3:
        return
    if topni[num-1][2] != topni[num][6]:
        move[num] = t
        toright(num+1, -1*t)

    
for _ in range(int(input())):
    which, to = map(int,input().split()) # which : 회전시킨 톱니바퀴 번호, to : 1 시계방향, -1 반시계방향
    real_which = which - 1
    move = [0 for _ in range(4)]
    move[real_which] = to

    toleft(real_which-1,-1*to)
    toright(real_which+1,-1*to)

    for i in range(4):
        if move[i] == 1:
            topni[i].appendleft(topni[i].pop())
        elif move[i] == -1:
            topni[i].append(topni[i].popleft())
        
    
ans = 0

for i in range(4):
   
    if int(topni[i][0]):
        tmp = 1<<i
        ans += tmp
    

print(ans)