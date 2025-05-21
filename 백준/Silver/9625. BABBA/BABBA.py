N = int(input())
dp = [[0,0]] * (N+1)
if N==1:
    print("0 1")
elif N==2:
    print("1 0")
else:
    dp[0] = [1,0]
    dp[1] = [0,1]
    for i in range(1, N):
        dp[i] = [dp[i-1][0]+dp[i-1][1], dp[i-1][0]]

    print(dp[N-1][1], dp[N-1][0])