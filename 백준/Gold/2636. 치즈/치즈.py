from collections import deque
def bfs(si, sj, v, idx):
    q = deque()

    q.append((si, sj))
    v[si][sj]=1
    cheese[si][sj]='#'

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if ni<0 or ni>=N or nj<0 or nj>=M:  continue
            if v[ni][nj]==1:    continue
            if arr[ci][cj]==1 and cheese[ni][nj]=='x':
                cheese[ci][cj]='#'
                continue
            elif arr[ni][nj]==1:
                cheese[ni][nj]=idx

            q.append((ni,nj))
            v[ni][nj]=1

def bfs_cheese(si, sj, v):
    q = deque()

    q.append((si, sj))
    v[si][sj]=1
    cheese[si][sj]='x'

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 \
                and arr[ni][nj]==0:
                    q.append((ni,nj))
                    v[ni][nj]=1
                    cheese[ni][nj]='x'

def print_arr(arr):
    for i in range(len(arr)):
        print(*arr[i])
    print()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# # 가장 자리에 벽 세우기
# for i in range(N):
#     for j in range(M):
#         if i==0 or i==N-1 or j==0 or j==M-1:
#             arr[i][j]=2
#
# print_arr(arr)
T = 0
left_cheese = []
first_cheese = sum(map(sum, arr))
while sum(map(sum, arr))>0:
    T+=1
    cheese = [[0]*M for _ in range(N)]
    v = [[0]*M for _ in range(N)]
    bfs_cheese(0,0,v)
    #print_arr(cheese)

    #--------------------------

    v = [[0]*M for _ in range(N)]
    idx=1
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1 and v[i][j]==0:
                bfs(i, j, v, idx)
                idx+=1
    #print_arr(cheese)

    for i in range(N):
        for j in range(M):
            if cheese[i][j]=='#':
                cheese[i][j]=0
                arr[i][j]=0
            elif cheese[i][j]=='x':
                cheese[i][j]=0

    #print_arr(cheese)
    #print_arr(arr)
    left_cheese.append(sum(map(sum, arr)))
    #print("-----------------")

print(T)
if len(left_cheese)>=2:
    print(left_cheese[-2])
else:
    print(first_cheese)