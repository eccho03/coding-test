import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def cal_dis(ti,tj):
    return abs(ti-ei) + abs(tj-ej)

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: int(x)-1, input().split()) # 1씩 감소시켜 받기
    arr[i][j]-=1 # 같은 위치에 여러 명 있을 수도 있으므로

ei,ej =map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11 # 비상구 위치

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j

def find_square(arr):
    mn = N
    # [1] 비상구와 모든 사람 간의 가장 짧은 또는 가로 세러 거리 구하기
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람인 경우
                mn = min(mn, max(abs(ei-i), abs(ej-j)))
    # [2] 모두 순회하면서 길이 L인 정사각형에 비상구와 위치 구하기
    for si in range(N-mn):
        for sj in range(N-mn): # 가능한 모든 시작위치
            if si<=ei<=si+mn and sj<=ej<=sj+mn: # 비상구가 포함된 위치
                for i in range(si, si+mn+1):
                    for j in range(sj, sj+mn+1):
                        if -11 < arr[i][j] < 0:
                            return si, sj, mn+1

ans = 0
cnt = M # 탈출 못한 생존자 수
for _ in range(K): # K턴 반복
    # [1] 모든 참가자 (동시에) 한 칸 이동(출구 최단 거리 방향)
    narr = [x[:] for x in arr] # 좌변에 들어가는 것은 다 narr에다가 함
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                cur_dis = cal_dis(i, j)
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0:  # 벽이 없는 곳으로 이동 가능
                        move_dis = cal_dis(ni, nj)  # 이동 위치에서 출구 거리 계산
                        if cur_dis > move_dis:  # 더 짧아질 때에만 이동
                            ans += arr[i][j] # 현재 좌표의 인원수가 이동함
                            narr[i][j] -= arr[i][j] # 동시 이동이니까 0으로 하는 게 아닌 변위만큼!
                            if arr[ni][nj] == -11: # 비상구라면 => 탈출
                                cnt += arr[i][j]
                            else:
                                narr[ni][nj] += arr[i][j]
                            break
    arr = narr
    if cnt == 0: break

    # [2] 미로 회전
    # 시계방향 90도: 같은 크기 -> 좌상단 행,열 / 내구도 -1
    si, sj, L = find_square(arr) # 비상구, 사람 포함 최소 정사각형
    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+(L-j-1)][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1 # 벽이면 회전시 1 감소

    arr = narr
    # 회전으로 달라졌으므로 비상구 위치 저장
    ei, ej = find_exit(arr)

print(-ans)
print(ei+1, ej+1)