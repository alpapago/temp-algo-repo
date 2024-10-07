n = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()


def plus(arr):
    bigger = []
    smaller = []
    answer = 0
    m = len(arr)
    # 짝수인 경우
    if m // 2 == 0:
        for i in range(m // 2):
            smaller.append(-arr[i])
        smaller.sort()
        for i in range(m // 2, m):
            bigger.append(arr[i])
        answer = smaller[m // 2 - 1] + bigger[m // 2 - 1]
        for i in range(m // 2 - 1):
            answer += 2 * (smaller[i] + bigger[i])
        return answer
    else:
        for i in range(m // 2 + 1):
            smaller.append(-arr[i])
        for i in range(m // 2 + 1, m):
            bigger.append(arr[i])

        for i in range(len(bigger)):
            answer += 2 * bigger[i]

        answer += smaller[0] + smaller[-1]
        for j in range(1, m // 2):
            answer += smaller[j]
        return answer


ans = plus(arr)
print(ans)
