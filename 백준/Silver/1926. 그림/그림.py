N,M = map(int,input().split())
picture = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
def bfs(si, sj, v):
    q = deque()
    area = 0

    q.append((si,sj))
    v[si][sj]=1
    area+=1

    while q:
        ci,cj = q.popleft()

        # 네방향, 범위내, 미방문, 조건=picture[ni][nj]==1
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and picture[ni][nj]==1:
                q.append((ni,nj))
                v[ni][nj]=1
                area+=1
    return area


mx_area = 0
picture_cnt = 0
v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if picture[i][j]==1 and v[i][j]==0:
            area = bfs(i,j,v)
            picture_cnt += 1
            if mx_area < area:
                mx_area = area
print(picture_cnt)
print(mx_area)