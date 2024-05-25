import heapq

n, m, k = map(int, input().split())

infected = list(map(int, input().split()))  # k개의 감염된 컴퓨터

logs = []
series = []

# 파일 전송 로그
for _ in range(m):
    # t시간에 a컴퓨터에서 b컴퓨터로
    heapq.heappush(series, list(map(int, input().split())))

while True:
    t, a, b = heapq.heappop(series)
    if a in infected:
        print(a)
        break
