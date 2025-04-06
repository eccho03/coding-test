K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split())) # 유적의 벽면 숫자
ans = [] # 정답은 라운드마다 출력해야 함

def rotate_piece(arr, si, sj):
    narr = [x[:] for x in arr] # arr 복사
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j]=arr[si+3-j-1][sj+i]
    return narr

def count_piece(arr, clr):
    v = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                cnt += bfs(i, j, v, arr, clr)

    return cnt

def bfs(si, sj, v, arr, clr):
    q = []
    cnt = 0
    piece = set()

    q.append((si, sj))
    piece.add((si, sj))
    v[si][sj] = 1
    cnt += 1

    while q:
        ci, cj = q.pop(0)

        # 범위내, 미방문, 조건: 현재와 전이 같을 때
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0 and arr[ci][cj]==arr[ni][nj]:
                q.append((ni, nj))
                piece.add((ni, nj))
                v[ni][nj]=1
                cnt += 1

    if cnt >= 3:
        if clr: # 만약에 진행하려는 조각이라면
            for i,j in piece:
                arr[i][j] = 0
        return cnt
    else:
        return 0

for _ in range(K): # K턴 진행
    mx_cnt = 0
    # [1] 탐사 진행
    for rot in range(1, 4): # 90, 180, 270 (항상 회전)
        for sj in range(0, 3): # 열
            for si in range(0, 3): # 행
                narr = [x[:] for x in arr] # 회전 전 항상 배열 복사
                for _ in range(rot): # rot 수만큼 반복
                    narr = rotate_piece(narr, si, sj)

                tmp = count_piece(narr, 0) # 실제 x
                if mx_cnt < tmp:
                    mx_cnt = tmp
                    marr = narr

    if mx_cnt == 0: break # 유물을 획득할 수 없었다면 바로 종료

    # [2] 연쇄 획득
    cnt = 0
    arr = marr
    while True:
        tmp = count_piece(marr, 1) # 실제 o
        if tmp == 0: break # 유물을 획득할 수 없을 때까지 연쇄적으로 획득
        cnt += tmp

        # 빈 곳에 채워넣기
        for j in range(0, 5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)
    ans.append(cnt)

print(*ans)