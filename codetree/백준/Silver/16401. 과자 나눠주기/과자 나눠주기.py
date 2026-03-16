M, N = map(int, input().split())

snacks = list(map(int, input().split()))
#print(snack)

start, end = 1, max(snacks)
ans = 0

while start <= end:
    mid = (start+end)//2

    cnt = 0
    # 현재 과자 길이 - mid
    for snack in snacks:
        if snack >= mid:
            cnt += snack//mid
            #print(snack, end=' ')

    if cnt >= M:
        start = mid+1
        ans = mid
    else:
        end = mid-1

    #print(": ",mid)

print(ans)