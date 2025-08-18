import heapq
def dijkstra(start):
    pq = []
    INF = float('inf')
    dists = [INF]*(D+1)

    heapq.heappush(pq, (0, start))
    dists[start]=0

    while pq:
        cur_dis, cur_node = heapq.heappop(pq)

        if cur_dis>dists[cur_node] or dists[cur_node]>D:
            continue

        for nxt_dis, nxt_node in graph[cur_node]:
            if nxt_dis+cur_dis < dists[nxt_node]:
                heapq.heappush(pq, (nxt_dis+cur_dis, nxt_node))
                dists[nxt_node] = nxt_dis+cur_dis
    return dists

N, D = map(int, input().split())

ways = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(D+1)]

for start, end, dist in ways:
    if end>D:   continue
    graph[start].append([dist, end])

for i in range(D):
    graph[i].append([1, i+1])

# print(graph)

dist = dijkstra(0)
print(dist[D])