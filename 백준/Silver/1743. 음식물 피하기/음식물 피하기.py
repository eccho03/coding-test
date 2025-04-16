from collections import deque
def bfs(si, sj, v):
    q = deque()
    cnt = 0

    q.append((si,sj))
    v[si][sj]=1
    cnt += 1

    while q:
        ci,cj = q.popleft()

        # 네방향, 범위내, 미방문, 조건: arr[ni][nj]==1
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt += 1
    return cnt

N, M, K = map(int, input().split())
lst = [list(map(lambda x: int(x)-1, input().split())) for _ in range(K)]
arr = [[0] * M for _ in range(N)]
for (i, j) in lst:
    arr[i][j]=1

mx_cnt = 0
v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]== 1:
            cnt = bfs(i,j,v)
            if cnt > mx_cnt:
                mx_cnt = cnt
print(mx_cnt)
