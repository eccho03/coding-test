T = int(input())

for _ in range(T):
    N = int(input())
    invests = list(map(int, input().split()))
    profit = 0 # 이익

    interval_mx = 0
    for i in range(N-1, -1, -1):
        if invests[i] > interval_mx:
            interval_mx = invests[i]
        else:
            profit += interval_mx - invests[i]
    print(profit)