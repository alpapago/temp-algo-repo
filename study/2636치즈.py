import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
pan = list()
visited = [[False for _ in range(m)] for _ in range(n)]
tot = list()

for _ in range(n):
    pan.append(list(map(int, input().split())))

for r in range(n):
    for c in range(m):
        if pan[r][c] == 1:
            tot.append([r, c])


def bfs():

    q = deque([(0,0)])
    tmp = deque([])
    visited[0][0] = 1

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_r = now_r + dr
            next_c = now_c + dc

            if 0 > next_r or next_r >= n or 0 > next_c or next_c >= m:
                continue

            if not visited[next_r][next_c]:
                visited[next_r][next_c] = 1
                # 치즈가 아니면
                if pan[next_r][next_c] == 0:
                    q.append((next_r,next_c))
                # 치즈면
                if pan[next_r][next_c] == 1:
                    tmp.append((next_r, next_c))
    cnt = 0
    while tmp:
        r, c = tmp.popleft()
        # 방문처리
        pan[r][c] = 0
        cnt += 1
    
    return cnt

t = 0
ans = 0
while True:
    visited = [[0] * m for _ in range(n)]

    tmp = bfs()
   
    if tmp == 0:
        print(t,ans, sep='\n')  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    ans = tmp
    t += 1