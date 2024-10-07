import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, s = input().split()
    n = int(n)

    ans = ""
    for i in range(len(s)):
        for _ in range(n):
            ans += s[i]
    print(ans)
