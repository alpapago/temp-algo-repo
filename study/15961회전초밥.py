import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
dishes = []

# n개의 줄에 접시
for _ in range(n):
    dishes.append(int(input()))

# 접시를 double
dishes = dishes + dishes

check = []
end = k
tmp = dishes[:end]

visited = [0]*(d+1)
# print(visited,len(visited),'ddjdjdjdj')
visited[c] = 1
max_len = 0
now_len = k

for i in range(len(tmp)):
    if not visited[tmp[i]]:
        visited[tmp[i]] = 1
    else:
        visited[tmp[i]] += 1
        now_len -= 1

max_len = now_len

for i in range(1,n):
    f = tmp.pop(0)
    visited[f] -= 1
    if visited[f]>=1:
        now_len += 1
    
    tmp.append(dishes[end])
    if not visited[dishes[end]]:
        visited[dishes[end]] = 1
    else:
        visited[dishes[end]] += 1
        now_len -= 1
    end += 1
    max_len = max(max_len, now_len)

print(max_len+1)