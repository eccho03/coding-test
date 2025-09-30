T, W = map(int, input().split())
nums = [int(input()) for _ in range(T)]

dp = [[0]*(W+1) for _ in range(T+1)]
# dp[T][W] 시간/이동횟수

for t in range(1, T+1):
    if nums[t-1]==1:
        dp[t][0] = dp[t-1][0]+1
    else:
        dp[t][0] = dp[t-1][0]

    for w in range(1, W+1):
        if nums[t-1]==2 and w%2==1: # 이동 o
            dp[t][w] = max(dp[t-1][w-1], dp[t-1][w])+1
        elif nums[t-1]==1 and w%2==0: # 이동 o
            dp[t][w] = max(dp[t-1][w-1], dp[t-1][w])+1
        else:
            dp[t][w] = max(dp[t-1][w-1], dp[t-1][w])

print(max(dp[T]))