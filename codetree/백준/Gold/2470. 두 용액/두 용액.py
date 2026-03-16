N = int(input())
arr = list(map(int, input().split()))

arr.sort()

start, end = 0, N-1

mn_start, mn_end = -1,-1
mn_dif = float('inf')

while start<end:
    tmp = arr[start]+arr[end]

    if abs(tmp)<mn_dif:
        mn_start, mn_end = start, end
        mn_dif = abs(tmp)

    if tmp < 0:
        start+=1
    elif tmp > 0:
        end-=1
    else:
        break

print(arr[mn_start], arr[mn_end])