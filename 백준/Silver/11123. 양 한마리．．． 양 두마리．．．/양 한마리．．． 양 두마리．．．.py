from collections import deque
def bfs(si, sj):
    q = deque()
    cnt = 0

    q.append((si,sj))
    v[si][sj]=1
    cnt+=1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]=='#':
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        tmp = list(input())
        arr.append(tmp)

    v = [[0]*M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j]=='#' and v[i][j]==0:
                ans = bfs(i, j)
                cnt+=1

    print(cnt)

