def find_me(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='I':
                return (i,j)

from collections import deque
def bfs(si,sj):
    q = deque()
    v = [[0]*M for _ in range(N)]
    cnt = 0

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()
        if arr[ci][cj]=='P':
            cnt+=1

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!='X':
                q.append((ni,nj))
                v[ni][nj]=1
    return cnt

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

si,sj = find_me(arr)
cnt = bfs(si,sj)
if cnt!=0:
    print(cnt)
else:
    print("TT")