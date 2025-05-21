N = int(input())

if N==0:
    print(1)
elif N==1:
    print(1)
else:
    dp = [0] * (N+1)
    dp[0]=1

    for n in range(1,N+1):
        for i in range(n):
            #print(i+1, i, n-i-1)
            dp[n] += dp[i]*dp[n-i-1]
    print(dp[N])