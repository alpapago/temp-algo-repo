import collections
    
dp = collections.defaultdict(int)

def climbStairs(n:int)->int:
    
    if n <= 2:
        return n
    
    # dp[n] 값이 이미 저장이 되어 있다면,
    elif dp[n]:
        return dp[n]
    
    dp[n] = climbStairs(n-1) + climbStairs(n-2)
    
    return dp[n]

print(climbStairs(3))