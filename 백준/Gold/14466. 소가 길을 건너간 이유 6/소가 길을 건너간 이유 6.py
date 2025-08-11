from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((si, sj))
    v[si][sj]=1

    while q:
        ci, cj = q.popleft()
        # print(ci, cj)
        if (ci, cj)==(ei, ej):
            return True

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and (ni,nj) not in graph[ci][cj]:
                q.append((ni, nj))
                v[ni][nj]=1

    return False

N, K, R = map(int, input().split())
grasslands = [list(map(lambda x: int(x)-1, input().split())) for _ in range(R)]
cow_locs = [list(map(lambda x: int(x)-1, input().split())) for _ in range(K)]

graph = [[[] for _ in range(N)] for _ in range(N)]
for r1, c1, r2, c2 in grasslands:
    graph[r1][c1].append((r2,c2))
    graph[r2][c2].append((r1,c1))

# print(graph)

ans = 0
for i in range(K):
    si, sj = cow_locs[i]
    for j in range(i, K):
        ei, ej = cow_locs[j]

        if (si, sj)!=(ei, ej):
            # print(i, j)
            is_reached = bfs(si, sj, ei, ej)
            if not is_reached:
                ans += 1

print(ans)