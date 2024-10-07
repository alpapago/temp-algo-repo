from collections import deque

# n 도시갯수, m 도로갯수, k거리정보,x 출발 도시의 번호

n, m, k, x = map(int, input().split())

adj = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)


def bfs(start):
    q = deque([start])
    visited = [0 for _ in range(n + 1)]
    visited[start] = 0

    while q:
        now = q.popleft()
        for next in adj[now]:
            if visited[next] == 0:
                visited[next] = visited[now] + 1
                q.append(next)


arr = bfs(x)
answer = []
for i in range(len(arr)):
    if arr[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    print(answer)
