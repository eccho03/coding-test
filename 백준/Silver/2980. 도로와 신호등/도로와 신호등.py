def state_light(time, r, g):
    # 빨간불
    if time % (r+g) <= r:
        return True

    # 초록불
    return False

N, L = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
# print(info)

time = 0
loc = 0 # 현재 위치
idx = 0

while loc < L:
    # print(idx)
    if idx < N:
        d, r, g = info[idx]

        # 해당 신호등 도착
        if d==loc:
            # 초록불
            if not state_light(time, r, g):
                loc += 1
                time += 1
            else:
                time += r - time%(r+g)
            idx += 1
            continue
    loc += 1
    time += 1

print(time)

