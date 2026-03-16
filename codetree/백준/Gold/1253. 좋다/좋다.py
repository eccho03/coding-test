N = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0

for i in range(N):
    cur = arr[i]
    start, end = 0, N-1
    while start<end:
        if start==i:
            start+=1
            continue
        if end==i:
            end-=1
            continue

        if arr[start]+arr[end]==cur:
            cnt+=1
            break
        elif cur<arr[start]+arr[end]:
            end-=1
        else:
            start+=1

print(cnt)