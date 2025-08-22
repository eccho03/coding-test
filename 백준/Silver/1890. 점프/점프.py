def dfs(ci, cj):
    global cnt
    if (ci,cj)==(ei,ej):
        return 1
    if v[ci][cj]!=-1:
        return v[ci][cj]

    v[ci][cj]=0
    for di,dj in directions:
        ni,nj = ci+di*arr[ci][cj], cj+dj*arr[ci][cj]
        if 0<=ni<N and 0<=nj<N:
            v[ci][cj] += dfs(ni,nj)
    return v[ci][cj]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

si,sj, ei,ej = 0,0, N-1,N-1

directions = [(1,0),(0,1)] # 하, 우
v = [[-1]*N for _ in range(N)]
ans = dfs(si, sj)
print(ans)