from collections import deque
import copy

n,m = map(int,input().split())

pan = []
# 0은 빈 칸 1은 벽
for _ in range(n):
    pan.append(list(map(int,input().split())))

# 좌표
dot = []
for _ in range(m):
    x, y = map(int,input().split())
    dot.append((x-1, y-1))

ans = 0

q = deque()
ans = 0
q.append([dot[0][0],dot[0][1],[(dot[0][0],dot[0][1])],1])

while q:
    now_x, now_y, history, idx = q.popleft()
    
    if idx >= m :
        break

    before_x = dot[idx-1][0]
    before_y = dot[idx-1][1]
    after_x = dot[idx][0]
    after_y = dot[idx][1]

    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        new_x = now_x + dx
        new_y = now_y + dy

        tmp = copy.deepcopy(history)
        if 0 > new_x or 0 > new_y or new_x >=n or new_y >= n:
            continue
        if pan[new_x][new_y]:
            continue
        if idx >= m:
            continue
        # 4사분면
        if before_x < after_x and before_y < after_y:
            if after_x < new_x or after_y < new_y:
                continue
        # 3사분면
        elif before_x < after_x and before_y > after_y:
            if after_x < new_x or after_y > new_y:
                continue
        # 2사분면
        elif before_x > after_x and before_y < after_y:
            if after_x > new_x or after_y < new_y:
                continue
        # 1사분면
        elif before_x > after_x and before_y > after_y:
            if after_x > new_x or after_y > new_y:
                continue

        if (new_x, new_y) not in history:
            if new_x == after_x and new_y == after_y:
                idx += 1
            if idx == m:
                ans += 1
                continue
            tmp.append((new_x, new_y))
            q.append((new_x,new_y,tmp,idx))

print(ans)