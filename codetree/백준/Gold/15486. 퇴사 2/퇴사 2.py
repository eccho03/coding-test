# N일 동안 상담 많이
N = int(input())
days = [[0,0]]+[list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+2)

for i in range(1,N+1):
    ti, pi = days[i]

    dp[i] = max(dp[i], dp[i-1])
    if i+ti > N+1:    continue
    dp[i+ti] = max(dp[i+ti], dp[i]+pi)

print(max(dp))
