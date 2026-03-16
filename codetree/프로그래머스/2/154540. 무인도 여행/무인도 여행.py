def solution(maps):
    from collections import deque
    def bfs(si, sj, v):
        q = deque()
        num = 0
        
        q.append((si, sj))
        v[si][sj]=1
        num += int(arr[si][sj])
        
        while q:
            ci, cj = q.popleft()
            
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = ci+di, cj+dj
                
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!='X':
                    q.append((ni, nj))
                    v[ni][nj]=1
                    num += int(arr[ni][nj])
        return num
        
    
    answer = []
    arr = []
    for m in maps:
        arr.append(list(m))
    # print(arr)
    
    N, M = len(arr), len(arr[0])
    v = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if v[i][j]==0 and arr[i][j]!='X':
                ground = bfs(i, j, v)
                # print(ground)
                answer.append(ground)
    if len(answer)>0:
        return sorted(answer)
    else:
        return [-1]