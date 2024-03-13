import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())
arr = []

# 노선
for _ in range(m):
    a,b,c = map(int,input().split())
    arr.append((a,b,c))

q = []
distance = [sys.maxsize]*(n+1)

#초기화
distance[1] = 0

for _ in range(m-1):
    for s,e,w in arr:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + w:
            distance[e] = distance[s] + w
        
isCycle = False

for s,e,w in arr:
    if distance[s] != sys.maxsize and distance[e] > distance[s] + w:
        isCycle = True

if not isCycle:
    for i in range(2,n+1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)