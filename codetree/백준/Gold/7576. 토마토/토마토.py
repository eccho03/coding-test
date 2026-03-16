from collections import deque
def bfs(q):
    cnt=1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and box[ni][nj]==0:
                q.append((ni,nj))
                box[ni][nj]=box[ci][cj]+1

        #myprint(box)
    return -1

def check():
    flag = 0
    for i in range(N):
        for j in range(M):
            if box[i][j]==0:
                #아직 익지않은 토마토있음
                flag=1
                break
    return flag

def one_day():
    q = deque()

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i,j))
    bfs(q)
    if check()==1:
        print(-1)
    else:
        res = 0
        for i in range(N):
            for j in range(M):
                res = max(res, box[i][j])
        print(res-1)


def myprint(arr):
    for i in range(N):
        print(*arr[i])
    print()

def already(arr):
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                flag=1
    return flag

M, N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]

if already(box)==1:
    one_day()
else:
    print(0)
