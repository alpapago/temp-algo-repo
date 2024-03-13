import sys
import heapq

input = sys.stdin.readline

n = int(input())  # 도시갯수
m = int(input()) # 버스갯수

arr = [[] for _ in range(n+1)] 
distance = [sys.maxsize]*(n+1)

for _ in range(m):
    start,end,w = map(int,input().split())
    arr[start].append((w,end))

s,e = map(int,input().split())
q = []
distance[s] = 0
visited = [False]*(n+1)

heapq.heappush(q,(0,s))

while q:
    now_w, now_v = heapq.heappop(q)
    # if distance[now_v] < now_w:
    #     continue
    if visited[now_v]:
        continue
    visited[now_v] = 1
    for next_w, next_v in arr[now_v]:
        next_ = now_w + next_w
        if distance[next_v] > next_:
            distance[next_v] = next_
            heapq.heappush(q,(distance[next_v],next_v))

print(distance[e])