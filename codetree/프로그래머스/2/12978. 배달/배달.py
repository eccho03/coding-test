import heapq

def solution(N, road, K):
    def dijkstra(start):
        dist[start]=0
        pq = []
        
        heapq.heappush(pq, (0, start))
        
        while pq:
            cur_dist, cur_node = heapq.heappop(pq)
            
            if cur_dist>dist[cur_node]:
                continue
            
            for nxt_dist, nxt_node in graph[cur_node]:
                if nxt_dist+cur_dist<dist[nxt_node]:
                    dist[nxt_node]=nxt_dist+cur_dist
                    heapq.heappush(pq, (nxt_dist+cur_dist, nxt_node))
    
    
    answer = 0
    INF = float('inf')
    dist = [INF]*(N+1)
    graph = [[] for _ in range(N+1)]
    for start, end, dis in road:
        graph[start].append((dis, end))
        graph[end].append((dis, start))
    
    dijkstra(1)
    # print(dist)
    for d in dist[1:]:
        if d<=K:
            answer+=1

    return answer