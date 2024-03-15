import sys
import heapq
input = sys.stdin.readline

m, n = map(int,input().split())
board = list()

for _ in range(n):
    tmp = input()
    t_list = list()
    for i in range(m):
        t_list.append(int(tmp[i]))
    board.append(t_list)

q = []
heapq.heappush(q,(0,0,0))
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

while q:
    now_ans,nr,nc = heapq.heappop(q)
    if nr == n-1 and nc == m-1:
        print(now_ans)
        break
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_r = nr + dr
        new_c = nc + dc
        if 0 > new_r or 0 > new_c or new_r >= n or new_c >= m:
            continue
        if not visited[new_r][new_c]:
            visited[new_r][new_c] = 1
            
            if board[new_r][new_c] == 0:
                heapq.heappush(q,(now_ans,new_r,new_c))
            elif board[new_r][new_c] == 1:
                heapq.heappush(q,(now_ans+1,new_r,new_c))
        