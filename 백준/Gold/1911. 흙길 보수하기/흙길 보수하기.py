N, L = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort()
ans = 0
idx = 0 # 현재까지 온 위치

for start, end in info:
    if idx>start:
        start=idx

    if end<=idx:
        continue # 새로 안 덮어도 커버 가능

    if (end-start)%L==0:
        cnt = (end-start)//L
    else:
        cnt = (end-start)//L+1
    ans += cnt
    idx = start+cnt*L


print(ans)
