N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]  # 공격한 턴수를 기록(최근공격 체크)

def building_cnt():
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0:
                cnt +=1
    return cnt

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

from collections import deque
def bfs(si,sj,ei,ej):
    q = deque()
    v = [[[] for _ in range(M)] for _ in range(N)]

    q.append((si,sj))
    v[si][sj]=(si,sj)

    while q:
        ci,cj = q.popleft()
        if (ci,cj)==(ei,ej):
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj)==(si,sj):
                    return True
                fset.add((ci,cj))

        # 네방향, 미방문, 조건: > 0
        for dr in range(4): # 우 하 좌 상
            ni,nj = ci+di[dr], cj+dj[dr]
            if ni<0 or ni>=N or nj<0 or nj>=M: # 가장자리인 경우 반대편으로 나옴
                dr = (dr+2)%4
                ni, nj = ci + di[dr], cj + dj[dr]
            if arr[ni][nj] <= 0:  continue  # 부서진 포탑인 경우 패스

            if len(v[ni][nj])==0:
                q.append((ni,nj))
                v[ni][nj]=(ci,cj)
    return False

def bomb(si,sj,ei,ej):
    bdi = [0, 1, 0, -1, -1, -1, 1, 1]
    bdj = [1, 0, -1, 0, -1, 1, -1, 1]

    arr[ei][ej] = max(0, arr[ei][ej]-arr[si][sj])
    for dr in range(8):
        ci,cj = (ei+bdi[dr])%N, (ej+bdj[dr])%M
        if arr[i][j]<=0:    continue # 부서진 포탑
        arr[ci][cj] = max(0, arr[ci][cj]-arr[si][sj]//2)
        fset.add((ci,cj))

for T in range(1, K+1): # K턴 반복
    if building_cnt()==1: # 포탑 개수 하나면 즉시 중지
        break
    mn, mx_turn, si, sj = 5001, 0, -1, -1
    # [1] 공격자 선정
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0:  continue # 포탑이 아님
            if mn > arr[i][j] or (mn == arr[i][j] and turn[i][j] > mx_turn)\
                or (mn == arr[i][j] and turn[i][j] == mx_turn and i+j > si+sj)\
                or (mn == arr[i][j] and turn[i][j] == mx_turn and i+j == si+sj and j>sj):
                mn,mx_turn,si,sj = arr[i][j],turn[i][j],i,j

    # [2] 공격 대상자 선정
    mx, mn_turn, ei, ej = 0, 1001, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0:  continue # 포탑이 아님
            if mx < arr[i][j] or (mx == arr[i][j] and turn[i][j] < mn_turn)\
                or (mx == arr[i][j] and turn[i][j] == mn_turn and i+j < ei+ej)\
                or (mx == arr[i][j] and turn[i][j] == mn_turn and i+j == ei+ej and j<ej):
                mx,mn_turn,ei,ej = arr[i][j],turn[i][j],i,j

    # 공격 전, 공격자 공격력 up!!
    arr[si][sj] += (N+M)
    turn[si][sj] = T
    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))

    # [3] 레이저 공격
    if bfs(si,sj,ei,ej)==False:
        bomb(si,sj,ei,ej)
    else:
        for i,j in fset:
            if (i,j)==(ei,ej):
                arr[i][j]=max(0, arr[i][j]-arr[si][sj])
            elif (i,j)==(si,sj):
                pass
            else:
                arr[i][j] = max(0, arr[i][j] - arr[si][sj]//2)

    # print(fset)
    # print(arr)
    # 공격과 무관했던 포탑 공격력 1씩 증가
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:    continue
            if (i,j) not in fset:
                arr[i][j]+=1

print(max(map(max, arr)))