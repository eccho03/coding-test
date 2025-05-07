from collections import deque
def bfs(si,sj,v):
    q = deque()

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,-1),(-1,-1),(1,1)):
            ni,nj = ci+di,cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                q.append((ni,nj))
                v[ni][nj]=1



N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and v[i][j]==0:
            bfs(i,j,v)
            ans+=1
print(ans)