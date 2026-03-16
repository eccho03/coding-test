T = int(input())
for _ in range(T):
    N = int(input())

    if N==0 or N==1:
        print(1)
    elif N==2:
        print(2)
    elif N==3:
        print(4)
    else:
        dp = [0] * (N+1)

        dp[0], dp[1] = 1, 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

        print(dp[N])