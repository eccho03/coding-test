N, M, shark_cnt = map(int, input().split())
shark_info = []
arr = [[[] for _ in range(M)] for _ in range(N)]

for _ in range(shark_cnt):
    r, c, s, d, z = map(int,input().split())
    shark_info.append((r-1,c-1,s,d-1,z))
    arr[r-1][c-1].append((s, d-1, z))

# 낚시왕 오른쪽으로 한 칸 이동
# 땅과 가장 가까운 상어 잡기
# 상어 이동 - 한 칸에 상어 두마리 이상이면 잡아먹기

def find_target(idx):
    target = []
    for r, c, s, d, z in shark_info:
        if c==idx:
            target.append((r,c,s,d,z))

    if target:
        target.sort(key=lambda x: x[0])
        return target[0]
    else:
        return -1

direction_change_row = {2:3, 3:2}
direction_change_col = {0:1, 1:0}
def move_once(r, c, s, d):
    # 상 하 우 좌
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    dr,dc = directions[d]
    if d==0 or d==1:  # 세로
        if N>1:
            s= s%(2*(N-1))
        else:
            s=0
        nr = r+dr*s
        while nr<0 or nr>=N:
            if nr<0:
                nr=-nr
            elif nr>=N:
                nr = 2*(N-1)-nr
            d=direction_change_col[d]
        return nr, c, d
    else:  # 가로
        if M>1:
            s=s%(2*(M-1))
        else:
            s=0
        nc = c + dc * s
        while nc<0 or nc>=M:
            if nc<0:
                nc=-nc
            elif nc >= M:
                nc =2*(M-1)-nc
            d=direction_change_row[d]
    return r, nc, d

def shark_move(sharks):
    new_arr = [[[] for _ in range(M)] for _ in range(N)]
    for r, c, s, d, z in sharks:
        nr, nc, nd = move_once(r, c, s, d)
        new_arr[nr][nc].append((s, nd, z))
    return new_arr

def kill_shark(arr):
    new_sharks = []
    for i in range(N):
        for j in range(M):
            if len(arr[i][j])==0:   continue
            if len(arr[i][j])>1:
                arr[i][j].sort(reverse=True, key=lambda x: x[-1]) # 크기 기준 정렬
            s, d, z = arr[i][j][0]
            arr[i][j] = [(s, d, z)]
            new_sharks.append((i, j, s, d, z))
    return new_sharks

ans = 0
for i in range(M): # 낚시왕 한 칸씩 이동
    shark = find_target(i) # 땅과 가장 가까운 상어 잡기
    if shark!=-1:
        r, c, s, d, z = shark
        shark_info.remove(shark) # 상어 삭제
        ans += z
        # print(arr)
        arr[r][c].remove((s, d, z))

    arr  = shark_move(shark_info)
    shark_info = kill_shark(arr)
    # print(shark_info)
    # print(arr)

print(ans)