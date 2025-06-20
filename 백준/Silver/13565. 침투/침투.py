from collections import deque
def bfs(si, sj, v):
    q = deque()

    q.append((si, sj))
    v[si][sj]=1

    while q:
        ci, cj = q.popleft()
        if ci== N-1:
            return True

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni,nj = ci+di, cj+dj

            # 범위내, 미방문, 네방향, 조건=흰색물질
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]=='0':
                q.append((ni, nj))
                v[ni][nj]=1

    return False


N, M = map(int, input().split())
arr = []
for _ in range(N):
    tmp = list((input()))
    arr.append(tmp)

# print(arr)

flag = False

v = [[0]*M for _ in range(N)]
for i in range(M):
    if arr[0][i]=='0' and v[0][i]==0:
        flag = bfs(0, i, v)
        if flag:
            break

if flag:
    print("YES")
else:
    print("NO")