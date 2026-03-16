from collections import deque
def bfs(si, sj):
    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        if arr[ci][cj]==-1:
            return True

        # 오른쪽/아래로만 이동 가능
        for di, dj in  ((1,0),(0,1)):
            ni, nj = ci+di*arr[ci][cj], cj+dj*arr[ci][cj]

            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=0:
                q.append((ni,nj))
                v[ni][nj]=1

    return False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# print(arr)

if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")