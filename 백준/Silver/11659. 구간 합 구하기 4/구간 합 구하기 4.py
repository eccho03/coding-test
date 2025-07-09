N, M = map(int, input().split())
num = list(map(int, input().split()))
info = []
for _ in range(M):
    i, j = map(int, input().split())
    info.append([i, j])

sum_num = [0]
for i in range(N):
    sum_num.append(sum_num[i] + num[i])

for cur in range(M):
    i, j = info[cur]
    # print(i, j)
    result = sum_num[j] - sum_num[i-1]
    print(result)
