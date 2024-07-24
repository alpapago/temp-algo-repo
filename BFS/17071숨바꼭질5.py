from collections import deque

n, k = map(int, input().split())

time = 0
q = deque([(n, time, k)])
# 방문처리
flag = False

while q:
    now_q, t, now_k = q.popleft()

    if now_k + t > 500000:
        break
    if now_q == now_k + t:
        flag = True
        time = t
        break
    for new_q in [now_q + 1, now_q - 1, now_q * 2]:
        if 0 <= new_q <= 500000:
            q.append((new_q, t + 1, now_k + t))

if flag:
    print(time)
else:
    print(-1)
