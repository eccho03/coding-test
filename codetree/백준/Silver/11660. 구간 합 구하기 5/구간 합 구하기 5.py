N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]

# print(arr)
# print(info)
prefix_sum = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i-1][j-1]
# print(prefix_sum)

for i in range(M):
    x1, y1, x2, y2 = info[i]

    # print(x1, y1, x2, y2)
    ans = prefix_sum[x2][y2] - (prefix_sum[x1-1][y2] + prefix_sum[x2][y1-1]) + prefix_sum[x1-1][y1-1]
    print(ans)
