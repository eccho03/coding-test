type = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def cal(tlst):

    visited = [[False] * m for _ in range(n)]

    for i in range(cnt):
        sx, sy = cctv[i] # 현재 위치
        rot = tlst[i] # 회전
        ty = arr[sx][sy] # cctv 타입

        for dir in type[ty]:
            ndir = (dir + rot) % 4
            cx, cy = sx, sy

            while True:
                cx, cy = cx + dx[ndir], cy + dy[ndir]

                if cx < 0 or cx >= n or cy < 0 or cy >= m:
                    break
                if arr[cx][cy] == 6:
                    break

                visited[cx][cy] = True

    sagak_cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 0:
                sagak_cnt += 1

    return sagak_cnt


def dfs(n, tlst):
    global ans
    if n == cnt:
        ans = min(ans, cal(tlst))
        return

    dfs(n + 1, tlst+[0]) # 0도 회전
    dfs(n + 1, tlst+[1]) # 90도 회전
    dfs(n + 1, tlst+[2]) # 180도 회전
    dfs(n + 1, tlst+[3]) # 270도 회전

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cctv.append((i, j))

ans = n*m
cnt = len(cctv)
dfs(0, [])
print(ans)