N = int(input())

if N==0:
    print(1)
elif N==1:
    print(1)
else:
    dp = [0] * (N+1)
    dp[0]=1

    for i in range(1,N+1):
        for j in range(0, i):
            #print(i, i-1, i-j-1)
            dp[i] += dp[j] * dp[i-j-1]
    print(dp[N])