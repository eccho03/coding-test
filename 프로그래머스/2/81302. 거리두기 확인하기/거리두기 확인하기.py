def solution(places):
    N = 5
    answer = []
    
    from collections import deque
    def bfs(si, sj, ei, ej):
        q = deque()
        v = [[0]*N for _ in range(N)]
        
        q.append((si,sj, 0))
        v[si][sj]=1
        
        while q:
            ci, cj, dist = q.popleft()
            if (ci, cj)==(ei, ej):
                return dist
            
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = ci+di, cj+dj
                
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!='X':
                    q.append((ni, nj, dist+1))
                    v[ni][nj]=1
        return -1
    
    def find_pi_pj(arr):
        p_lst = []
        for i in range(N):
            for j in range(N):
                if arr[i][j]=='P':
                    p_lst.append((i, j))
        return p_lst
    
    for place in places:
        arr = []
        for p in place:
            tmp = list(p)
            arr.append(tmp)
        # print(arr)
        
        p_lst = find_pi_pj(arr)
        # print(p_lst)
        flag=True
        
        for i in range(len(p_lst)):
            for j in range(len(p_lst)):
                if i==j: continue
                # print(p_lst[i], p_lst[j])
                si, sj = p_lst[i]
                ei, ej = p_lst[j]
                dist = bfs(si, sj, ei, ej)
                # print(dist)
                
                if dist!=-1 and dist<=2:
                    flag=False
                    break
            if not flag:
                break
                
        answer.append(1 if flag else 0)
        
        
    
    return answer