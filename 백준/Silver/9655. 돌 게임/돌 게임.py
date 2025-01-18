n = int(input())
stone = [1, 3]
dp = [0] * 1001

for i in range(0, 1001):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        turn = 'SK'
        dp[i] = min(dp[i], dp[i-1]+3)
        
    else:
        turn = 'CY'
        dp[i] = min(dp[i], dp[i-1]+3)
    if dp[i] == n:
        break
print(turn)