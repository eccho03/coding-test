import heapq
from collections import deque, defaultdict


def dijkstra(start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0 # 시작 노드 ~ 자기 자신
    pq = [(0, start)]

    while pq:
        cur_dis, cur_node = heapq.heappop(pq)
        if cur_node == end:
            return dist

        # 이미 처리된 노드 무시
        if cur_dis > dist[cur_node]:
            continue

        for nxt_node, nxt_dis in graph[cur_node].items():
            distance = cur_dis + nxt_dis

            if distance < dist[nxt_node]:
                dist[nxt_node] = distance
                heapq.heappush(pq, (distance, nxt_node))

    return dist

N, M, X = map(int, input().split())
street = [list(map(int, input().split())) for _ in range(M)]

graph = defaultdict(dict)
for start, end, time in street:
    graph[start][end] = time

#print(graph)
mx_time = -1
for i in range(1, N+1):
    start = dijkstra(i, X)
    end = dijkstra(X, i)
    if mx_time < (start[X]+end[i]):
        mx_time = start[X]+end[i]
print(mx_time)