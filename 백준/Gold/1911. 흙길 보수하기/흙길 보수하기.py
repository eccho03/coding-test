import math

N, L = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort()
ans = 0
idx = 0

for start, end in info:
    # print(start, end)

    if idx>start:
        start=idx

    if idx>=end:
        continue # 커버 가능

    cnt = math.ceil((end-start)/L)
    ans += cnt   # 널빤지 개수
    idx = start + L*cnt
    # print(idx)

print(ans)
