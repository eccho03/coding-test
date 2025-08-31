N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0]=1

for i in range(N):
    for j in range(N):
        if dp[i][j]==0: continue
        if arr[i][j] == 0: continue

        ni,nj = i+arr[i][j], j+arr[i][j]
        if ni < N:
            dp[ni][j] += dp[i][j]

        if nj < N:
            dp[i][nj] += dp[i][j]


print(dp[N-1][N-1])
