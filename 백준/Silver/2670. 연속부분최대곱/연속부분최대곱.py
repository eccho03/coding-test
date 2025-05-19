N = int(input())
num = [float(input()) for _ in range(N)]

#print(num)

dp = [0] * N
dp[0] = num[0]
for i in range(1,N):
    dp[i] = max(num[i], dp[i-1]*num[i])

ans = max(dp)
print("{:.3f}".format(ans))