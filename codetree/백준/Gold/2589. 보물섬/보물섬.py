import sys
from collections import deque

def bfs(si, sj):
    q = deque()
    v = [[0]*M for _ in range(N)]

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()

        # 범위내, 네방향, 미방문, 조건=육지
        for di,dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]=='L':
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return v

N, M = map(int, input().split())

arr = []
for _ in range(N):
    tmp = list(input())
    arr.append(tmp)

# print(arr)

lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            lst.append((i, j))

# ans = bfs(3,0,4,1)
# print(ans)

mx_dist = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            v = bfs(i, j)
            mx_dist = max(mx_dist, max(map(max, v)))

print(mx_dist-1)