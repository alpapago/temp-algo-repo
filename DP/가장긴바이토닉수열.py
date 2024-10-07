"""
 11054번 가장 긴 바이토닉 수열 문제

 1)최장 증가 부분 수열의 길이구하기
    1-1) 부분 수열의 길이를 dp_asc 에 저장

 2)최장 감소 부분 수열의 길이구하기
    2-1) 부분 수열의 길이를 dp_des 에 저장

 3)각 원소를 중심으로 각 부분 수열 길이의 합을 구하고 최대값 구하기

 단, 증가부분수열과 감소부분수열에서 중심원소가 2번 더해지므로 최종 합에서 1을 뺴주어야 한다. 
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(" ")))
reverse_arr = arr.copy()[::-1]

dp_asc = [1] * n
dp_des = [1] * n

# 1) 최장 증가 부분 수열의 길이구하기
# 1-1) 부분 수열의 길이를 dp_asc 에 저장
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_asc[i] = max(dp_asc[j] + 1, dp_asc[i])

# 2)최장 감소 부분 수열의 길이구하기
# 2-1) 부분 수열의 길이를 dp_des 에 저장
# 단, 감소 부분 수열 구할때는 reverse 된 arr를 하나 더 copy해서 reverse_arr로 선언한 후 사용
for i in range(n):
    for j in range(i):
        if reverse_arr[i] > reverse_arr[j]:
            dp_des[i] = max(dp_des[i], dp_des[j] + 1)

# 3)원소를 중심으로 각 부분 수열 길이의 합을 계산하고 최대값 구하기
# 단, 증가부분수열과 감소부분수열에서 중심원소가 2번 더해지므로 최종 합에서 1 뺸다.
answer = 0
for i in range(n):
    tmp = dp_asc[i] + dp_des[n - 1 - i] - 1
    answer = max(tmp, answer)

print(answer)
