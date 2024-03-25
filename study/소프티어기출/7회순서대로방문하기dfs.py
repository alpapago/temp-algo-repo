import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pan = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    pan.append(tmp)

jum = list()
for _ in range(m):
    x,y = map(int,input().split())
    jum.append((x-1,y-1))

ans = 0

def dfs(points, depth):
    global ans

    if depth == m:
        ans += 1
        return 

    r = points[-1][0]
    c = points[-1][1]
    # print(points,'경로',ans,'ans')

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = dr + r
        nc = dc + c
        if 0 > nr or 0 > nc or n <= nr or n <= nc:
            continue
        if pan[nr][nc] == 1:
            continue
        if (nr,nc) not in points:
            if nr == jum[depth][0] and nc == jum[depth][1]:
                # print(depth,'depth_1')
                dfs(points +[(nr,nc)], depth + 1)
            else:
                # print(depth,'depth_2')
                dfs(points+[(nr,nc)], depth)

check = []
check.append((jum[0][0],jum[0][1]))
dfs(check,1)

print(ans)    