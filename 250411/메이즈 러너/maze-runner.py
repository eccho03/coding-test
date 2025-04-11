def cnt_surviver():
    for i in range(N):
        for j in range(N):
            if -10<=arr[i][j]<=-1: # 남은 참가자 있음
                return True
    return False

def cal_distance(x,y):
    return abs(x-ei)+abs(y-ej)

def find_square(arr):
    # rx, ry, rd 찾기 (rx 좌표 작고, ry좌표 작은 순)
    for l in range(1, N + 1):  # 한변 크기(1 ~ N)
        for rx in range(0, N - l + 1):
            for ry in range(0, N - l + 1):
                people_include = False
                for i in range(N):
                    for j in range(N):
                        if -10<=arr[i][j]<=-1:
                            if rx <= i < rx + l and ry <= j < ry + l:
                                people_include = True

                if people_include and (rx <= ei < rx + l and ry <= ej < ry + l):
                    # 출구 포함 & 참가자 최소 1명 포함 체크
                    return rx, ry, l

    return -1, -1, -1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j]==-11:
                return i,j
    return -1,-1

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: int(x)-1, input().split()) # 1씩 감소시켜 받기
    arr[i][j]-=1 # 같은 위치에 여러 명 있을 수도 있으므로

ei,ej =map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11 # 비상구 위치

ans = 0
for _ in range(K): # K턴 반복
    # [1] 모든 참가자 (동시에) 한 칸 이동(출구 최단 거리 방향)
    narr = [x[:] for x in arr] # 좌변에 들어가는 것은 다 narr에다가 함
    for i in range(N):
        for j in range(N):
            if -10<=arr[i][j]<=-1:
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if ni<0 or ni>=N or nj<0 or nj>=N:  continue
                    if 1<=arr[ni][nj]<=9:   continue    # 벽이거나 범위를 벗어난 경우
                    cur_dis = cal_distance(i, j)
                    move_dis = cal_distance(ni, nj)  # 이동 위치에서 출구 거리 계산
                    if cur_dis > move_dis:  # 더 짧아질 때에만 이동
                        ans += arr[i][j] # 현재 좌표의 인원수가 이동함
                        narr[i][j] -= arr[i][j] # 동시 이동이니까 0으로 하는 게 아닌 변위만큼!
                        if arr[ni][nj] != -11: # 비상구 아니면: 탈출 x
                            narr[ni][nj] += arr[i][j]
                        break

    arr=narr
    # 모든 참가자가 탈출했으면 즉시 종료
    if cnt_surviver() == False:
        break

    # [2] 미로 회전
    si,sj,L = find_square(arr)
    narr = [x[:] for x in arr]

    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-1-j][sj+i]
            if 1<=narr[si+i][sj+j]<=9:
                narr[si+i][sj+j]-=1 # 회전된 벽 내구도 -1

    arr=narr

    # 회전으로 달라진 비상구 위치 저장
    ei,ej = find_exit(arr)

print(-ans)
print(ei+1,ej+1)