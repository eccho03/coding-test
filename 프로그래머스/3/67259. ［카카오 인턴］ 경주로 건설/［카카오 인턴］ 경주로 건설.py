def solution(board):
    answer = 0
    
    '''
    (0,0) -> (N-1, N-1)
    
    0: 칸 비어있음
    1: 벽
    
    0-based
    상하좌우 네 방향
    
    직선 도로: 상하 / 좌우 연결
    코너: 두 직선 도로가 서로 직각으로 만남
    
    건설 비용
    - 직선 도로: 100원
    - 코너: 500원
    
    경주로 건설하는 데 필요한 최소 비용 -> 다익스트라?
    
    '''
    
    import heapq
    def bfs():
        pq = []
        INF = float('inf')
        v = [[[INF]*4 for _ in range(N)] for _ in range(N)]
        
        heapq.heappush(pq, (0, 0, 0, 1))
        heapq.heappush(pq, (0, 0, 0, 3))
        
        
        v[0][0][1]=0
        v[0][0][3]=0
        
        while pq:
            cost, ci, cj, cur_dir = heapq.heappop(pq)
            if (ci, cj)==(N-1, N-1):
                return cost, cur_dir
            if cost>v[ci][cj][cur_dir]: continue
            
            for dir in range(4):
                di, dj = directions[dir]
                ni, nj = ci+di, cj+dj
                
                if not (0<=ni<N and 0<=nj<N) or board[ni][nj]==1:
                    continue
                
                if cur_dir!=dir and cost+500+100< v[ni][nj][dir]:
                    heapq.heappush(pq, (cost+500+100, ni, nj, dir))
                    v[ni][nj][dir]=cost+500+100
                elif cur_dir==dir and cost+100 < v[ni][nj][dir]:
                    heapq.heappush(pq, (cost+100, ni, nj, dir))
                    v[ni][nj][dir]=cost+100
                    
        return -1, -1
    
    N = len(board)
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
    
    mn_cost, change_dir = bfs()
    # print(mn_cost, change_dir)
        
    
    return mn_cost