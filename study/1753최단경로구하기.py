import sys
import heapq

input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input()) # 출발노드

INF = 10*20000+1
distance = [INF]*(v+1)

my = [[] for _ in range(v+1)]
q = []

for _ in range(e):
    start,end,w = map(int,input().split())
    my[start].append((w,end))

# 현재까지 거리, 시작점
heapq.heappush(q, (0, k))
distance[k] = 0

while q:
    nowVal,nowNode = heapq.heappop(q)
    if distance[nowNode] < nowVal:
        continue

    for info in my[nowNode]:
        now_next_cost, next_idx = info
        next_idx_cost = nowVal + now_next_cost
        if next_idx_cost < distance[next_idx]:
            distance[next_idx] = next_idx_cost
            heapq.heappush(q, (next_idx_cost, next_idx))

       
for i in range(1,v+1):
    ans = distance[i]
    if ans == INF:
        ans = 'INF'
    print(ans)