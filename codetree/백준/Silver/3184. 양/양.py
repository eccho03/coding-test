from collections import deque
def bfs(si,sj,v,flag):
    q = deque()
    wolf_cnt = 0
    sheep_cnt = 0

    q.append((si,sj))
    v[si][sj]=1
    sheep_cnt+=1

    while q:
        ci,cj = q.popleft()
        if flag==1 and arr[ci][cj]=='v':
            arr[ci][cj]='.'
        elif flag==2 and arr[ci][cj]=='o':
            arr[ci][cj]='.'

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            # 범위내,네방향,미방문,조건=울타리가 아님 (늑대,빈칸)
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!='#':
                q.append((ni,nj))
                v[ni][nj]=1

                if arr[ni][nj]=='v': # 늑대라면
                    wolf_cnt+=1

                elif arr[ni][nj]=='o':
                    sheep_cnt+=1

    return wolf_cnt, sheep_cnt

def myarr(arr):
    for i in range(N):
        print(*arr[i])

def check_ans(arr):
    wolf_cnt, sheep_cnt = 0,0
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='v':
                wolf_cnt+=1
            elif arr[i][j]=='o':
                sheep_cnt+=1
    return sheep_cnt, wolf_cnt

N,M = map(int,input().split())

arr = []
for i in range(N):
    row = list(input())
    arr.append(row)

v = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='o' and v[i][j]==0:
            wolf_cnt, sheep_cnt = bfs(i,j,v, False)
            #print(wolf_cnt, sheep_cnt)

            v = [[0] * M for _ in range(N)]
            if sheep_cnt > wolf_cnt:
                wolf_cnt, sheep_cnt = bfs(i,j,v,1)
            else:
                wolf_cnt, sheep_cnt = bfs(i,j,v,2)

            #print(wolf_cnt, sheep_cnt)
#myarr(arr)

sheep_cnt, wolf_cnt = check_ans(arr)
print(sheep_cnt, wolf_cnt)