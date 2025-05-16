from collections import deque
def bfs(si,sj):
    q = deque()
    v = [[-1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                v[i][j]=0

    q.append((si,sj))
    v[si][sj]=0

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==-1:
                if arr[ni][nj]==1:
                    q.append((ni,nj))
                    v[ni][nj]=v[ci][cj]+1
                else:
                    v[ni][nj]=0
    return v

def find_target():
    for i in range(N):
        for j in range(M):
            if arr[i][j]==2:
                return i,j

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
#ans = []

ei,ej = find_target()

ans = bfs(ei,ej)

for i in range(len(ans)):
    print(*ans[i], end=' ')
    print()