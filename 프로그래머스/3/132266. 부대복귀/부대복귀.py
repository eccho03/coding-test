def solution(n, roads, sources, destination):
    import heapq
    def dijkstra(start):
        pq = []
        dist = [INF]*(n+1)
        
        heapq.heappush(pq, (0, start))
        dist[start]=0
        
        while pq:
            cur_dist, cur = heapq.heappop(pq)
            
            if cur_dist>dist[cur]:
                continue
            
            for nxt in graph[cur]:
                if cur_dist+1<dist[nxt]:
                    dist[nxt]=cur_dist+1
                    heapq.heappush(pq, (cur_dist+1, nxt))
        return dist
    
    
    answer = []
    
    # 강철부대 두 지역간의 길 통과시간 1
    # 최단시간 부대 복귀 필요
    
    graph = [[] for _ in range(n+1)]
    INF = float('inf')
    
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start) # 왕복 가능
    
    dist = dijkstra(destination)
    # print(dist)
    
    for source in sources:
        if dist[source]==INF:
            answer.append(-1)
        else:
            answer.append(dist[source])
    
    return answer