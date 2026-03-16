N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
interval_sum = 0

mn_len = float('inf')
for start in range(N):

    while interval_sum < S and end < N:
        interval_sum += arr[end]
        end += 1

    if interval_sum>=S:
        # print(arr[start:end])
        mn_len = min(mn_len, end-start)

    interval_sum -= arr[start]

if mn_len == float('inf'):
    print(0)
else:
    print(mn_len)