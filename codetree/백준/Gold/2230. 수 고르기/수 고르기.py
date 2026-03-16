N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
start, end = 0,1
mn_dif = float('inf')
arr.sort()

while end<N:
    cur_dif = arr[end]-arr[start]

    # print(arr[start], arr[end])
    if cur_dif>M:
        start+=1
        if cur_dif < mn_dif:
            mn_dif = cur_dif
    elif cur_dif<M:
        end+=1
    else:
        mn_dif = M
        break

print(mn_dif)