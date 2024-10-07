n = 6
times = [7, 10]
import heapq


def sol(n, times):

    cand = []
    cnt = 0
    for i in range(1, n // len(times) + 2):
        for j in range(len(times)):
            heapq.heappush(cand, i * times[j])

    answer = 0
    while cnt < n:
        answer = heapq.heappop(cand)
        cnt += 1

    return answer


print(sol(n, times))
