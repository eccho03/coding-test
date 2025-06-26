from collections import deque
def bfs():
    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((r1, c1))
    v[r1][c1] = 1

    while q:
        ci, cj = q.popleft()
        if (ci,cj)==(r2, c2):
            return v[ci][cj]-1

        for di, dj in ((-2, -1),(-2, 1),(0,-2),(0,2),(2,-1),(2,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1

    return -1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
ans = bfs()
print(ans)