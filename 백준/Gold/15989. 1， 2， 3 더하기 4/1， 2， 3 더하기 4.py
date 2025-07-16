T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0, 0, 0, 0] for _ in range(N+1)]

    if 1<=N<=3:
        print(N)
    else:
        dp[1][1], dp[1][2], dp[1][3] = 1, 1, 1
        dp[2][1], dp[2][2], dp[2][3] = 1, 2, 2
        dp[3][1], dp[3][2], dp[3][3] = 1, 2, 3

        for i in range(4, N+1):
            for j in (1,2,3):
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]

        print(dp[N][3])