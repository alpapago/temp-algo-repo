# n : 트럭 수 , w: 다리길이 l: 다리 최대 하중
from collections import deque

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque([0] * w)

now = 0
t = 0
for _ in range(n):
    now_truck = trucks.popleft()
    # 트럭이 다리위에 있을 동안
    while bridge:
        bridge.popleft()
        t += 1

        # 현재 다리 위 무게 + 현재 트럭 무게 < 최대하중
        if sum(bridge) + now_truck <= l:
            bridge.append(now_truck)
            break
        # 최대하중보다 크다면
        else:
            bridge.append(0)

print(t + w)

"""
while 각각의 차에 대해서,

    if (다리 위 하중 합 + 차의 하중) <= 최대하중:
        차를 다리위에 추가
        break
    else:
        0을 다리위에 추가

"""
