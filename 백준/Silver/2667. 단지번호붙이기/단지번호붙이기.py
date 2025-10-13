N = int(input())
arr = [list(str(input())) for _ in range(N)]

from collections import deque
def bfs(si, sj, v):
    q = deque()
    house_cnt = 0

    q.append((si, sj))
    v[si][sj]=1
    house_cnt += 1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]=='1':
                q.append((ni, nj))
                v[ni][nj]=1
                house_cnt += 1

    return house_cnt

v = [[0]*N for _ in range(N)]
total_cnt = 0
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j]=='1' and v[i][j]==0:
            house_cnt = bfs(i, j , v)
            total_cnt += 1
            ans.append(house_cnt)

print(total_cnt)
ans.sort()
for a in ans:
    print(a)