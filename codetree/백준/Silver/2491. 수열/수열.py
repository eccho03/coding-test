N = int(input())

arr = list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = 1

    if arr[i-1]<=arr[i-2]:
        dp[i] = dp[i-1]+1

smaller = (max(dp))

dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = 1

    if arr[i-1]>=arr[i-2]:
        dp[i] = dp[i-1]+1

bigger = max(dp)

print(max(smaller, bigger))