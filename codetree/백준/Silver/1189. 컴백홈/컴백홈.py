def dfs(si, sj, dis):
    global cnt
    v[si][sj]=1
    #print(arr[si][sj], end=' ')
    #print(f'si:{si}, sj:{sj}, 거리:{dis}')


    if (si,sj)==(0,M-1) and dis==K:
        cnt+=1

    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si+di, sj+dj

        if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!='T':
            v[ni][nj]=1
            dfs(ni,nj, dis+1)
            v[ni][nj]=0



N, M, K = map(int, input().split())
arr = []
cnt = 0
for i in range(N):
    tmp = list(input())
    arr.append(tmp)
# print(arr)
v = [[0] * M for _ in range(N)]
dfs(N-1, 0, 1)

print(cnt)