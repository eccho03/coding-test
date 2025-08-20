def solution(n, m, x, y, r, c, k):
    answer = ''
    
    import heapq
    def bfs():
        pq = []
        v = set()
        
        heapq.heappush(pq, ('',x,y,0))
        v.add((x,y,0))
        
        while pq:
            cur_ans,ci,cj,dist = heapq.heappop(pq)
            if (ci,cj)==(r,c) and dist==k:
                return cur_ans
            elif dist>k:
                continue
            
            for i in range(4):
                di, dj = directions[i]
                ni,nj=ci+di,cj+dj
                nxt_ans = cur_ans+dir[i]
                if 0<=ni<n and 0<=nj<m and (ni,nj,dist+1) not in v:
                    heapq.heappush(pq, (nxt_ans,ni,nj,dist+1))
                    v.add((ni,nj,dist+1))
        return "impossible"
    
    x, y, r, c = x-1, y-1, r-1, c-1 # 0-based
    dir=['l','r','u','d']
    directions=[(0,-1),(0,1),(-1,0),(1,0)]
    
    xy_rc_dist = abs(x-r)+abs(y-c)
    if xy_rc_dist>k or (k - xy_rc_dist) % 2 != 0:
        return "impossible"
    
    answer = bfs()
    
    return answer