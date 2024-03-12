import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    value = sorted(tmp)

    docs = deque([(i, idx) for idx, i in enumerate(tmp)])

    cnt = 1
    while True:
        i, idx = docs.popleft()
        val = value.pop()
        if val == i:
            if idx == m:
                print(cnt)
                break
            continue
        docs.append((i, idx))
        value.append(val)
        cnt += 1
