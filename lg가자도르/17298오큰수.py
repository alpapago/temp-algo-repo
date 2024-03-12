n = int(input())
nums = list(map(int, input().split()))

ans = []
stack = []

for i in range(n - 1, -1, -1):
    # 앞에서부터 탐색하면 탐색만 O(n^2)이 되므로 뒤에서 부터 탐색해야함.
    now = nums[i]
    while True:
        # 걔보다 더 큰수는 없을때
        if not stack:
            ans.append(-1)
            stack.append(now)
            break
        # 스택에 수가 있을 때,
        else:
            if stack[-1] > now:
                ans.append(stack[-1])
                stack.append(now)
                break
            else:
                stack.pop()

for i in range(n - 1, -1, -1):
    print(ans[i], end=" ")
