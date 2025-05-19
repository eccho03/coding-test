from collections import deque
def bfs(si, sj):
    q = deque()
    v = [[0]*M for _ in range(N)]
    lst = []

    q.append((si,sj,0))
    v[si][sj]=1

    while q:
        ci,cj,cnt = q.popleft()
        if arr[ci][cj]==1 and (ci,cj)!=(si,sj):
            #lst.append(cnt-1)
            return cnt

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
                q.append((ni,nj, cnt+1))
                v[ni][nj]=1

    #return lst
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx_dis = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            dis = bfs(i, j)
            #print(dis)
            if dis!=-1:
                mx_dis = max(mx_dis, dis)

print(mx_dis)
