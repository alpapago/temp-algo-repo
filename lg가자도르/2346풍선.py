from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
balloon = list(map(int, input().split()))
balloons = deque([])
for idx, i in enumerate(balloon):
    balloons.append((i, idx))

ans = []
while balloons:
    now, idx = balloons.popleft()
    ans.append(idx)
    if not balloons:
        break
    elif now > 0:
        for _ in range(now - 1):
            balloons.append(balloons.popleft())
    else:
        for _ in range(-now):
            balloons.appendleft(balloons.pop())

for i in ans:
    print(i + 1, end=" ")
