N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]

info.sort(key=lambda x: x[0])
mn_set = info[0][0]
info.sort(key=lambda x: x[1])
mn_one = info[0][1]

# print(mn_set, mn_one)

# 세트가 더 싼 경우
if mn_one > mn_set//6:
    if mn_set < (N%6)*mn_one:
        print(mn_set*(N//6+1))
    else:
        print(mn_set*(N//6) + mn_one*(N%6))
# 낱개가 더 싼 경우
else:
    print(mn_one*N)