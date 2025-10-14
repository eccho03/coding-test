import math
def solution(players, m, k):
    answer = 0
    dp = [0]*24
    
    for t in range(24):
        n = players[t]
        
        if t-k>=0:
            dp[t-k]=0
        
        x=n//m-sum(dp)
        
        if n//m>=1 and x>0:
            dp[t]+=x
            answer+=dp[t]        
    
    return answer