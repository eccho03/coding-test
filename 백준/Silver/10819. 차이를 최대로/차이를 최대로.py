from itertools import permutations
def dfs(idx, total, arr):
    global mx_val
    if idx == N-1:
        mx_val = max(mx_val, total)
        return

    dfs(idx+1, total+abs(arr[idx]-arr[idx+1]), arr)
    dfs(idx+1, total, arr)


mx_val = 0
N = int(input())
arr = list(map(int, input().split()))

for i in permutations(arr, N):
    narr = list(i)
    dfs(0, 0, narr)
print(mx_val)