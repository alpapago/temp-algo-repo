from collections import deque

n, k = map(int, input().split())

dist = [0 for _ in range(100001)]

q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        print(dist[now])
        exit(0)

    for new in [now + 1, now - 1, now * 2]:
        if 0 <= new <= 100000 and not dist[new]:
            dist[new] = dist[now] + 1
            # 여기서 가지치기 하면 case가 다 안담김..
            q.append(new)
