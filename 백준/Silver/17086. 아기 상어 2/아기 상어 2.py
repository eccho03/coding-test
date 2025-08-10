from collections import deque
def bfs(si, sj):
    q = deque()
    v = [[0]*M for _ in range(N)]

    q.append((si, sj, 0))
    v[si][sj]=1

    while q:
        ci, cj, dist = q.popleft()

        if arr[ci][cj]==1:
            return dist

        for di, dj in ((-1, 0),(1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1), (1, 1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
                q.append((ni, nj, dist+1))
                v[ni][nj]=1

    return -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        ans[i][j] = bfs(i, j)

print(max(map(max, ans)))