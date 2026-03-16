T, W = map(int, input().split())
arr = [0] + [int(input()) for _ in range(T)]
dp = [[0]*(W+1) for _ in range(T+1)]

for i in range(1, T+1):
    # 자두나무는 초기에 1번 아래에 위치
    if arr[i]==1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W+1):

        cur_pos = 2 if j%2==1 else 1
        eat_cnt = 1 if arr[i]==cur_pos else 0
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+eat_cnt


print(max(dp[T]))
