def lp(s:str)->str:
    def expand(left:int,right:int)->str:
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 예외처리
    if len(s) <2 or s == s[::-1]:
        return s 
    
    result = ''
    # 모든 i 에 대해서 대칭하게 다 찾는거네
    for i in range(len(s)-1):
        result = max(result,
                        expand(i,i+1),
                        expand(i,i+2))
    
    return result

print(lp('babad'))