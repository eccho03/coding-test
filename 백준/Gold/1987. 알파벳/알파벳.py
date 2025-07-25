ans = 0
def dfs(i, j, cur, cnt):
    global ans

    # print(i, j, cur, cnt)
    ans = max(ans, cnt)

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i+di, j+dj

        if 0<=ni<R and 0<=nj<C and v[ni][nj]==0:
            if arr[ni][nj] not in cur:
                v[ni][nj]=1
                dfs(ni, nj, cur+arr[ni][nj], cnt+1)
                v[ni][nj]=0

R, C = map(int, input().split())
arr = []
for _ in range(R):
    tmp = list(input().rstrip())
    arr.append(tmp)

v =[[0]*C for _ in range(R)]
dfs(0, 0, arr[0][0], 1)
print(ans)