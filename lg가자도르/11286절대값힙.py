import sys
import heapq

input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    now = int(input())
    # 0입력받으면 최솟값 출력
    if now == 0:
        # heap이 비어있으면, 0 프린트
        if not heap:
            print(0)
        else:
            x, value = heapq.heappop(heap)
            print(value)
    else:
        heapq.heappush(heap, (abs(now), now))
