N, K = map(int, input().split())
alchols = [int(input()) for _ in range(N)]

# print(*alchol)
start, end = 1, max(alchols)
ans = 0

while start<=end:
    mid = (start+end)//2

    cnt = 0
    for jujeonja in alchols:
        cnt += jujeonja//mid

    if cnt >= K:
        ans = mid
        start = mid+1
    else:
        end = mid-1

print(ans)