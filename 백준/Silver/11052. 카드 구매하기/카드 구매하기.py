# 카드팩 종류 N가지 (1개, 2개, ... N개)
N = int(input())
P = [0]+list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]

# dp[i][t] = 1~i번 팩 사용해서 t장 만들 때 금액
for i in range(1,N+1):
    dp[i][0] = 0    # i번 0장 사용하면 0
    for t in range(1,N+1):
        dp[i][t] = dp[i-1][t]
        if t-i<0:   continue
        dp[i][t] = max(dp[i][t], dp[i][t-i]+P[i])

print(max(map(max, dp)))
