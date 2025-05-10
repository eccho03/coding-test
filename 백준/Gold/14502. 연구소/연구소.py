from collections import deque
from itertools import combinations
def bfs(si,sj,v,arr):
    q = deque()

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj

            # 빈칸일때 퍼져나감
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                arr[ni][nj]=2
                q.append((ni,nj))
                v[ni][nj]=1

def myarr(arr):
    for i in range(N):
        print(*arr[i])

def count_safe(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                cnt+=1
    return cnt

def virus_extend(arr):
    # 바이러스 확산
    v = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 바이러스라면 - 확산됨
            if v[i][j] == 0 and arr[i][j] == 2:
                bfs(i, j, v, arr)

def wall_target(arr):
    target = []
    mx_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                target.append((i,j))
    for i in combinations(target, 3):
        mx_cnt = max(make_wall(i), mx_cnt)
    print(mx_cnt)

def make_wall(s):
    #print(s)
    narr = [x[:] for x in arr]
    for ci,cj in s:
        narr[ci][cj]=1
    virus_extend(narr)
    cnt = count_safe(narr)

    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

wall_target(arr)
# myarr(arr)
# ans = count_safe(arr)
# print(ans)