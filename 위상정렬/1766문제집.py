"""
 1766번 문제집 문제

 1) 길이 n+1의 board 리스트 선언
    (먼저 푸는 것이 좋은 문제집 관계를 저장)

 2) 각 문제집의 위상을 저장하는 phase 리스트 선언
    [위상 순서]
        풀이 우선순위가 높은 순서(난이도 쉬운 문제, 먼저 푸는 것이 좋은 문제)로 위상이 높다
        (단, 위상이 높다 = 위상 값이 작다)

 3) 위상 값이 0으로 가장 위상이 높아서 먼저 풀어야 할 문제집을 heap으로 구현한 priority queue에 삽입한다.
    heap 자료구조를 사용하는 이유는 문제집 번호가 작을수록 먼저 풀어야 하기 때문이다.
    파이썬에서 heap은 min heap으로 구현되어 있다.

 4) 풀린 문제집은 answer에 저장하고 다음으로 풀어야 할 문제집들의 위상을 1 낮춘다.
    4-1) 만약 위상이 0이라 다음으로 풀어야 하는 문제집이라면, heap에 저장한다.
    4-2) 모든 문제집을 풀 때까지 반복문을 진행한다.

"""

import sys
import heapq

input = sys.stdin.readline

# 1 ~ n 까지의 문제집이 존재
# m : 먼저 풀면 좋은 문제들 경우의 수
n, m = map(int, input().split())

# 1) 길이 n+1의 board 리스트 선언 (먼저 푸는 것이 좋은 문제집 관계를 저장)
board = [[] for _ in range(n + 1)]

# 2) 각 문제집의 위상을 저장하는 phase 리스트 선언
phase = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)   # a번 문제집을 먼저 풀고 b번 문제집을 푸는 것이 좋으므로 board[a] 리스트에 문제집 b를 추가
    phase[b] += 1 # a는 b다음에 푸는 것이 좋으므로 b의 위상을 낮춘다.

# 3) 위상 값이 0으로 가장 위상이 높아서 먼저 풀어야 할 문제집을 heap으로 구현한 priority queue에 삽입한다.
#   heap 자료구조를 사용하는 이유는 문제집 번호가 작을수록 먼저 풀어야 하기 때문이다.
#   파이썬에서 heap은 min heap으로 구현되어 있다.
q = []
for i in range(1, n + 1):
    if phase[i] == 0:
        heapq.heappush(q, i)


answer = [] # 정답을 저장할 리스트 선언

# 4) 풀린 문제집은 answer에 저장하고 다음으로 풀어야 할 문제집들의 위상을 1 낮춘다.
#   4-1) 만약 위상이 0이라 다음으로 풀어야 하는 문제집이라면, heap에 저장한다.
#   4-2) 모든 원소를 방문할 때까지 반복문을 진행한다.
while q:
    now = heapq.heappop(q)
    answer.append(now)
    for i in board[now]:
        phase[i] -= 1
        if phase[i] == 0:
            heapq.heappush(q, i)

print(*answer)
