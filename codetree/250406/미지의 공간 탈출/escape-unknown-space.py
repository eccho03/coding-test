def find_3d_start():
    for i in range(M):
        for j in range(M):
            if arr3[4][i][j] == 2:
                return 4, i, j

def find_2d_end():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 4:
                arr[i][j] = 0 # pop을 확인해서 종료를 할 때 0으로 바꿈, 출발까지 확산하는 경우만 주의
                return i, j


def find_3d_base():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return i, j

def find_3d_end_2d_start():
    bi, bj = find_3d_base()
    for i in range(bi, bi+M):
        for j in range(bi, bi+M):
            if arr[i][j] != 3: continue
            # 네방향 확인
            for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
                ni, nj = i + di, j + dj
                if arr[ni][nj] == 0:
                    if di==-1 and dj==0:            # 상측
                        return 3, M-1, (M-1)-(j-bj), i-1,j
                    elif di==1 and dj==0:           # 하측
                        return 2, M-1, j-bj, i+1, j
                    elif di==0 and dj==-1:          # 좌측
                        return 1, M-1, i-bi, i, j-1
                    else:                           # 우측
                        return 0, M-1, (M-1)-(i-bi), i, j+1
    return -1, -1, -1

left_nxt = {0:2, 2:1, 1:3, 3:0}
right_nxt = {0:3, 2:0, 1:2, 3:1}
from collections import deque
def bfs_3d(sk, si, sj, ek, ei, ej):
    q = deque()
    v = [[[0]*M for _ in range(M)] for _ in range(5)]

    q.append((sk, si, sj))
    v[sk][si][sj] = 1

    while q:
        ck, ci, cj = q.popleft()

        if (ck, ci, cj) == (ek, ei, ej):
            return v[ck][ci][cj]

        # 네방향, 범위내/범위밖->다른 평면, 미방문
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci + di, cj + dj

            # 범위밖
            if ni < 0:  # 위쪽 범위 이탈
                if ck == 0: nk, ni, nj = 4, (M - 1) - cj, M - 1
                elif ck == 1: nk, ni, nj = 4, cj, 0
                elif ck == 2: nk, ni, nj = 4, M - 1, cj
                elif ck == 3: nk, ni, nj = 4, 0, (M - 1) - cj
                elif ck == 4: nk, ni, nj = 3, 0, (M - 1) - cj
            elif ni >= M:  # 아래쪽 범위이탈
                if ck == 4: nk, ni, nj = 2, 0, cj
                else: continue
            elif nj < 0:  # 왼쪽 범위이탈
                if ck == 4: nk, ni, nj = 1, 0, ci
                else: nk, ni, nj = left_nxt[ck], ci, M - 1
            elif nj >= M:  # 오른쪽 범위이탈
                if ck == 4: nk, ni, nj = 0, 0, (M - 1) - ci
                else: nk, ni, nj = right_nxt[ck], ci, 0
            else: nk = ck # 이탈 아니면 같은 평면

            # 미방문, 조건 - 장애물이 아니면
            if v[nk][ni][nj] == 0 and arr3[nk][ni][nj] == 0:
                q.append((nk, ni, nj))
                v[nk][ni][nj] = v[ck][ci][cj] + 1

    return -1
#dist = bfs_2d(v, dist, si, sj, ei, ej)
def bfs_2d(v, dist, si, sj, ei, ej):
    q = deque()

    q.append((si, sj))
    v[si][sj] = dist

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return v[ci][cj]

        # 네방향, 범위내, 미방문/조건 맞으면
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci + di, cj + dj

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and v[ni][nj] > v[ci][cj] + 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

    return -1

N, M, F = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr3 = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)] # 동/서/남/북/윗면

time = [list(map(int, input().split())) for _ in range(F)]

# [1] 주요 위치들 찾기
# 3차원 시작, 3차원 끝, 2차원 시작, 2차원 끝 좌표 탐색
sk_3d, si_3d, sj_3d = find_3d_start()
ei, ej = find_2d_end()
ek_3d, ei_3d, ej_3d, si, sj = find_3d_end_2d_start()

#print(ek_3d, ei_3d, ej_3d)

# # [2] 3차원 공간 탐색: 시작 위치 -> 탈출 위치 거리 탐색(BFS 최단거리)
dist = bfs_3d(sk_3d, si_3d, sj_3d, ek_3d, ei_3d, ej_3d)

# 동 서 남 북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

if dist != -1:
    #[3] 2차원 탐색 준비: 시간 이상 현상 처리
    v = [[float('inf')]*N for _ in range(N)]
    for ti,tj,td,tv in time: # 출구가 아닌 경우만 확산
        v[ti][tj]=1
        for mul in range(1, N+1):
            ti,tj = ti+di[td], tj+dj[td]
            if 0<=ti<N and 0<=tj<N and arr[ti][tj]==0 and (ti,tj)!=(ei,ej):
                v[ti][tj]=tv*mul
            else:
                break

    #[4] 2차원 시작 위치에서 탈출구 탐색
    dist = bfs_2d(v, dist, si, sj, ei, ej)
print(dist)