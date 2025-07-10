N, K = map(int, input().split())
arr = list(map(int, input().split()))
prefix_arr = [0]*(N+1)

for i in range(N):
    prefix_arr[i+1] = prefix_arr[i] + arr[i]

# print(prefix_arr)

# print(prefix_arr[2]-prefix_arr[1-1]) # 1~2 누적합
#       prefix_arr[3]-prefix_arr[2-1] # 2~3 누적합

ans = [0]*(N-K+1)
for i in range(N-K+1):
    ans[i] = prefix_arr[K+i] - prefix_arr[i+1-1]
print(max(ans))