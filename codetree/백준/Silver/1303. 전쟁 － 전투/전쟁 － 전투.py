from collections import deque
def bfs(si,sj,v):
    q = deque()
    cnt = 0

    q.append((si,sj))
    v[si][sj]=1
    cnt = 1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==arr[ci][cj]:
                # 조건 이렇게 걸어야 범용적으로 B, W 쓸 수 있음
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1

    return cnt

M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]
white_cnt = 0
blue_cnt = 0

v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='W' and v[i][j]==0:
            white = bfs(i,j,v)
            white_cnt += white**2
        elif arr[i][j]=='B' and v[i][j]==0:
            blue = bfs(i,j,v)
            blue_cnt += blue**2

print(white_cnt, blue_cnt)