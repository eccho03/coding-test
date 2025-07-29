N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
INF = 10**8
mn_set = INF
mn_one = INF

for i in range(M):
    s1, s2 = info[i]
    # print(s1, s2)
    if s1 < mn_set:
        mn_set = s1
    if s2 < mn_one:
        mn_one = s2

# print(mn_one, mn_set)
mn_money = INF

for one in range(N+1):
    for set in range(N+1):
        amount = one + set*6
        if amount < N:  continue
        mn_money = min(mn_money, mn_one*one + mn_set*set)

print(mn_money)

