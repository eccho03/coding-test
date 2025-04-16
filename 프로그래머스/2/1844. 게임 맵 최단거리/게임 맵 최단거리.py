from collections import deque
def bfs(arr, si, sj, N, M):
    q = deque()
    v = [[0]*M for _ in range(N)]
    
    q.append((si,sj))
    v[si][sj]=1
    
    while q:
        ci,cj = q.popleft()
        if (ci,cj)==(N-1,M-1):
            return v[ci][cj]
        
        # 네방향, 범위내, 미방문, 조건: arr[][]==1
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return -1
    
def solution(maps):
    answer = 0
    
    M = len(maps[0])
    N = len(maps)
    #print(N,M)
    
    answer = bfs(maps, 0, 0, N, M) # 0-based
    return answer