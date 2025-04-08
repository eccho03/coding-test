di = [-1, 0, 1, 0] # 상 우 하 좌
dj = [0, 1, 0, -1]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
players = {}
for i in range(1, M+1):
    x, y, d, s = map(int, input().split())
    players[i] = (x-1, y-1, d, s) # 좌표 0~N 0~N

guns = set()
init_point = [0 for _ in range(M+1)] # 플레이어의 현재 포인트
ans = [0 for _ in range(M+1)]

for i in range(1,M+1):
    init_point[i]=players[i][3]

def find_player(ti, tj):
    for i in range(1,M+1):
        pi, pj, pd, ps = players[i]
        if (pi, pj)==(ti, tj):
            return i, pi, pj, pd, ps
    return -1, -1, -1, -1, -1

def vs_player(pi,pj,pd,ps,ti,tj,td,ts):
    # t : 승리자 / p : 패배자
    # 이긴 플레이어 - 점수 획득
    ans[tidx] += ts - ps
    #print(ans)
    if (ti, tj) in guns:
        tmp_gun = []
        for (gi, gj, ga) in guns:
            if (ti, tj) == (gi, gj):
                tmp_gun.append((gi, gj, ga))
        if len(tmp_gun) >= 1:
            tmp_gun.sort(key=lambda x: x[2])  # 공격력 높은 순으로 정렬
            tar_gun = tmp_gun[0]
            guns.remove(tar_gun)
            ts += tmp_gun[0][2]
            players[idx] = (ti, tj, td, ts)

    # 진 플레이어의 이동
    ni, nj = pi + di[pd], pj + dj[pd]
    if ni < 0 or ni >= N or nj < 0 or nj >= N or (ni, nj) in players:
        # 이동하려는 칸에 1)다른 플레이어가 있는경우 2)격자 범위밖인경우
        for rot in range(1, 4):  # 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동
            ni, nj = pi + di[(pd + rot) % 4], pj + dj[(pd + rot) % 4]
    pi, pj = ni, nj
    tmp_gun = []
    for (gi, gj, ga) in guns:
        if (pi, pj) == (gi, gj):
            tmp_gun.append((gi, gj, ga))
    if len(tmp_gun) >= 1:
        tmp_gun.sort(key=lambda x: x[2])  # 공격력 높은 순으로 정렬
        tar_gun = tmp_gun[0]
        guns.remove(tar_gun)
        ps += tmp_gun[0][2]
        players[idx] = (ni, nj, pd, ps)
    #print(ni, nj, pd, ps)

for i in range(N):
    for j in range(N):
        if arr[i][j]>0: # 총이 있을 경우
            guns.add((i,j,arr[i][j])) # 총 목록에 넣기
            arr[i][j]=0

for _ in range(K):
    # 플레이어 한 명씩 돌면서 아래의 과정을 반복
    for idx in range(1, M+1):
        pi, pj, pd, ps = players[idx]
        # [1] 본인 방향대로 1칸 이동 (벗어나면 반대 방향)
        ni, nj = pi+di[pd], pj+dj[pd]
        if ni<0 or ni>=N: # 벗어났을 경우 반대 방향으로 이동
            ni = pi+di[(pd+2)%4]
        if nj<0 or nj>=N:
            nj = pj+dj[(pd+2)%4]

        tidx, ti, tj, td, ts = find_player(ni, nj) # 이동한 칸에서 플레이어 찾기
        players[idx] = (ni, nj, pd, ps)
        pi, pj = ni, nj

        # [2]-1 이동한 칸에 플레이어가 없을 경우 - 공격력 가장 높은 총만 획득
        if ti == -1:
            tmp_gun = []
            for (gi, gj, ga) in guns:
                if (pi, pj)==(gi, gj):
                    tmp_gun.append((gi, gj, ga))
            if len(tmp_gun)>=1:
                tmp_gun.sort(key=lambda x:x[2]) # 공격력 높은 순으로 정렬
                tar_gun = tmp_gun[0]
                guns.remove(tar_gun)
                ps += tmp_gun[0][2]
                players[idx] = (ni, nj, pd, ps)
            #print(players)

        # [2]-2 이동한 칸에 플레이어가 있을 경우 - 싸움!!
        else:
            if ps < ts:
                vs_player(pi, pj, pd, ps, ti, tj, td, ts)

            elif ps > ts:
                vs_player(ti, tj, td, ts, pi, pj, pd, ps)
            else:
                # 비기는 경우에는 초기 능력치 비교
                if init_point[idx] > init_point[tidx]:
                    vs_player(ti, tj, td, ts, pi, pj, pd, ps)
                else:
                    vs_player(pi, pj, pd, ps, ti, tj, td, ts)


        # 2-1) 이긴 플레이어 점수 획득

        # 2-2) 진 플레이어 이동 (오른쪽으로 90도씩 회전하면서 이동 가능 시 이동)

print(*ans[1:]) # 0번 플레이어는 없음