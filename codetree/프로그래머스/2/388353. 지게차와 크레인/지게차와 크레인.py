def solution(storage, requests):
    answer = 0
    N = len(storage)
    M = len(storage[0])
    new_storage = [['%']*(M+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(M):
            new_storage[i+1][j+1]=storage[i][j]
    
    
    def check(i, j):
        outside = check_outside()
        # print(outside)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=i+di, j+dj
            if (ni,nj) in outside:
                return True
        
        return False
            
    from collections import deque
    def check_outside():
        q = deque()
        v = [[0]*(M+2) for _ in range(N+2)]
        outside = []
        
        q.append((0,0))
        v[0][0]=1
        outside.append((0,0))
        
        while q:
            ci,cj=q.popleft()
            
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=ci+di,cj+dj
                
                if 0<=ni<N+2 and 0<=nj<M+2 and v[ni][nj]==0:
                    if arr[ni][nj]==0:
                        q.append((ni,nj))
                        v[ni][nj]=1
                        outside.append((ni,nj))
        return outside
    
    def print_arr(arr):
        for i in range(len(arr)):
            print(*arr[i])
        print()
        
    arr = [[0]*(M+2)] + [[0]+[1]*M+[0] for _ in range(N)]+[[0]*(M+2)]

    for request in requests:
        if len(request)==1:
            tmp_lst = []
            for i in range(N+2):
                for j in range(M+2):
                    if new_storage[i][j]==request:
                        if check(i, j)==True:
                            tmp_lst.append((i, j))
            
            for i, j in tmp_lst:
                new_storage[i][j]='%'
                arr[i][j]=0
        else:
            new_request = request[0]
            for i in range(N+2):
                for j in range(M+2):
                    if new_storage[i][j]==new_request:
                        new_storage[i][j]='%'
                        arr[i][j]=0

        # print_arr(new_storage)
        # print_arr(arr)
        # print("--------------")
    answer = sum(map(sum, arr))
    
    return answer