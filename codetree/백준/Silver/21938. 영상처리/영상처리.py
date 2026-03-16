from collections import deque
def bfs(si, sj):
    q = deque()

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            #범위내, 네방향, 미방문, 조건=pixel=255
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and screen[ni][nj]==255:
                q.append((ni, nj))
                v[ni][nj]=1

N, M = map(int, input().split())

screen = []
for i in range(N):
    info = list(map(int, input().split()))
    arr = []

    pixel=0
    for j in range(M*3):
        pixel+=info[j]
        if j%3==2:
            arr.append(pixel//3)
            pixel=0
    screen.append(arr)
T = int(input())

# print(screen)
for i in range(N):
    for j in range(M):
        if screen[i][j]>=T:
            screen[i][j]=255
        else:
            screen[i][j]=0

# print(screen)

v=[[0]*M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if screen[i][j]==255 and v[i][j]==0:
            bfs(i, j)
            cnt += 1

print(cnt)
