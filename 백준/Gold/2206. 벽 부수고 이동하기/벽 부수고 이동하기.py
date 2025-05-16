from collections import  deque
def bfs(si, sj):
    q = deque()
    v = [[[0]*2 for _ in range(M)] for _ in range(N)]

    q.append((si,sj,0,1))
    v[si][sj][0]=1

    while q:
        ci,cj,broke,dist = q.popleft()
        if (ci,cj)==(N-1,M-1):
            return dist

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                # 벽이 아닌 경우
                if arr[ni][nj]==0 and v[ni][nj][broke]==0:
                    q.append((ni,nj,broke,dist+1))
                    v[ni][nj][broke]=1
                elif arr[ni][nj]==1 and broke==0 and v[ni][nj][1]==0:
                    q.append((ni,nj,1,dist+1))
                    v[ni][nj][1] = 1

    return -1

def myarr(arr):
    for i in range(N):
        print(*arr[i])
    print()

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
ans = bfs(0,0)
print(ans)