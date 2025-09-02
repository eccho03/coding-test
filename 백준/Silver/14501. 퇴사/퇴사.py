# N일 동안 상담 많이
N = int(input())
days = [[0,0]]+[list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+2)


# dp[i] i번째 날부터 마지막날까지 최대수익
# print(days)

for i in range(1,N+1):
    t,p = days[i]

    dp[i] = max(dp[i],dp[i-1])
    if i+t<=N+1:
        dp[i+t] = max(dp[i+t], dp[i]+p)

print(max(dp))