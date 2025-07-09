def solution(info, n, m):
    MAX = 120
    
    d = [[False]*MAX for _ in range(MAX)]
    d[0][0] = True
    
    info_cnt = len(info)
    
    for i in range(info_cnt):
        nxt_dp = [[0]*MAX for _ in range(MAX)]
        trace_a, trace_b = info[i]
        
        for a in range(n):
            for b in range(m):
                if not d[a][b]:
                    continue
                
                if a + trace_a < n:
                    nxt_dp[a + trace_a][b] = True
                if b+ trace_b < m:
                    nxt_dp[a][b + trace_b] = True
        
        for a in range(n):
            for b in range(m):
                d[a][b] = nxt_dp[a][b]
        
    for a in range(n):
        for b in range(m):
            if d[a][b]:
                return a
    
    
    return -1