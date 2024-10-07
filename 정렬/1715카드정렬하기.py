import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    tmp = int(input())
    heapq.heappush(q, tmp)

answer = 0
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    answer += a + b
    heapq.heappush(q, (a + b))

print(answer)
