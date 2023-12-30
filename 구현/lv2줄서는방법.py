def factorial(N):
    dp = [1]
    for i in range(1, N + 1):
        dp.append(dp[-1] * i)
    
    return dp[-1]

def solution(n, k):
    answer = []

    number = [i for i in range(1,n + 1)]
    k -= 1
    while number:
        n -= 1
        num = factorial(n)
        idx, k = divmod(k,num)
        answer.append(number[idx])
        number.pop(idx)
        # number.remove(idx)
    return answer

print(solution(4,5)) # [3,1,2]