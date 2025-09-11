N, M = map(int, input().split())
chapters = [[0,0]]+[list(map(int, input().split())) for _ in range(M)]

MAX=300
dp = [[0]*(MAX+1) for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1,MAX+1):
        day, page = chapters[i]
        dp[i][j] = dp[i-1][j]

        if j-day>=0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-day]+page)

print(dp[M][N])