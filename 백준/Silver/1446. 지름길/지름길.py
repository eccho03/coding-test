import heapq
from collections import defaultdict
def dijkstra(start, D):
    dist = {i: float('inf') for i in range(D+1)}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dis, cur_node = heapq.heappop(pq)

        if cur_dis > dist[cur_node]:
            continue

        for nxt_node, nxt_dis in graph[cur_node].items():
            distance = cur_dis + nxt_dis

            if distance < dist[nxt_node]:
                dist[nxt_node] = distance
                heapq.heappush(pq, (distance, nxt_node))
    return dist

N, D = map(int, input().split())
drive =[list(map(int, input().split())) for _ in range(N)]
graph = defaultdict(dict)

# 지름길 아닌 일반길
for i in range(D):
    graph[i][i+1]=1

for start, end, l in drive:
    if end <= D:
        if end not in graph[start] or l <  graph[start][end]:
            graph[start][end] = l

#print(graph)

ans = dijkstra(0, D)
print(ans[D])