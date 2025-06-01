N, M = map(int, input().split())
days = list(int(input()) for _ in range(N))

start, end = max(days), sum(days)
K = 0

while start <= end:
    mid = (start+end)//2

    total = 0
    cnt = 0

    for day in days:
        if total < day:
            total = mid
            cnt += 1
        total -= day

    if cnt>M:
        start = mid+1
    else:
        end = mid-1
        K = mid
print(K)