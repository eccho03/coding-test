# 각 숫자별 필요한 성냥 개수
sticks = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

T = int(input())
for _ in range(T):
    N = int(input()) # 성냥 개수
    mn_N, mx_N = N, N

    '''
    3 - 7 7 
    6 - 6 111
    7 - 8 711
    15 - 108 7111111
    '''

    mn_num, mx_num = "", ""

    # 최댓값 구하기
    if mx_N%2==1:
        mx_num+='1'*(mx_N//sticks[1]-1)
        mx_N-=sticks[7]
        mx_num = '7'+mx_num
    else:
        mx_num+='1'*(mx_N//sticks[1])

    # 최솟값 구하기
    # 성냥 i개로 만들 수 있는 가장 작은 수
    if mn_N<=7:
        base = {2: "1", 3: "7", 4: "4", 5: "2", 6: "6", 7: "8"}
        mn_num = base[mn_N]
        # print(base[mn_N])
    else:
        INF =  "9"*(mn_N+1)
        dp = [INF]*(mn_N+1)
        dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = "1", "7", "4", "2", "6", "8"

        for i in range(8, mn_N+1):
            for digit in range(10):
                if i-sticks[digit]<2 or dp[i-sticks[digit]]==INF:
                    continue

                if len(dp[i-sticks[digit]]+str(digit)) < len(dp[i]) or \
                    len(dp[i-sticks[digit]]+str(digit))==len(dp[i]) and dp[i-sticks[digit]]+str(digit) < dp[i]:
                    dp[i] = dp[i-sticks[digit]]+str(digit)

        mn_num = dp[N]

    print(mn_num, mx_num)
