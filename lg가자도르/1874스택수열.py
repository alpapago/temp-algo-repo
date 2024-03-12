import sys

input = sys.stdin.readline

ans = []
# 숫자를 넣을 스택
stack = []
num = 1

flag = True

for _ in range(int(input())):
    n = int(input())

    while num <= n:
        stack.append(num)
        num += 1
        ans.append("+")
    if stack[-1] == n:
        stack.pop()
        ans.append("-")
    elif stack[-1] > n:
        flag = False
        break

if flag:
    print("\n".join(ans))
else:
    print("NO")
