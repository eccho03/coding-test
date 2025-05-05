from collections import deque
def bfs(si,sj):
    q = deque()
    cnt = 0

    q.append((si,sj))
    v[si][sj]=1
    cnt+=1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            # 범위내,네방향,미방문,조건: arr[ni][nj]==0
            ni,nj = ci+di, cj+dj

            if 0<=ni<M and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt



def myarr(arr):
    for i in range(M):
        print(*arr[i])

M,N,K = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(K)]

arr = [[0]*N for _ in range(M)]

for si,ei,sj,ej in paper:
    for i in range(ei,ej):
        for j in range(si,sj):
            arr[i][j]=1

v = [[0]*N for _ in range(M)]
ans = []
cnt = 0
for i in range(M):
    for j in range(N):
        if arr[i][j]==0 and v[i][j]==0:
            num = bfs(i,j)
            ans.append(num)
            cnt+=1

ans.sort()
print(cnt)
print(*ans)