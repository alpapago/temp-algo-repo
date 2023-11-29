## 코딩테스트에 필요한 파이썬 문법

# 1장
# 2장
# 3장
# 4장
# 5장

# 6장 문자열 조작

## 정렬 방법

### sort와 sorted 

# sort : 제자리 정렬(In-place Sort)
# sorted : 정렬 결과를 별도로 리턴
#   그래서 별도의 정렬 기준을 커스텀해서 지정할 수 있음.

# 예1)
c = ['ccc','aaaa','d','bb']
sorted(c,key=len) # 길이기준 오름차순으로 정렬
# ['d','bb', 'ccc', 'aaaa']

# 예2)
a = ['cde','cfc','abc']

# 문자열의 첫번째, 마지막 character 반환
def fn(s):
    return s[0],s[-1]

sorted(a,key=fn)
# ['abc','cfc','cde']

# 이거랑 같은 말
sorted(a,key = lambda x :(x[0],x[-1]))


# 7장 배열

# 1byte = 8 bit
# 32비트 머신 > 2^23 - 1까지 메모리 주소 표현할수잇음. === 최대 4GB 까지 인식
# 64비트 > 16EB

# max함수는 사전식(lexicographical)으로 정렬해서 가장 마지막꺼 return
# 근데 key=len으로 key함수 설정해주면, 길이가 긴 string도 return 해준다.

s1 ='a'
s2 = 'cbb'
s3 = 'abbbabab'
print(max(s1,s2,s3)) # cbb
print(max(s1,s2,s3,key=len)) # abbbabab
