import heapq
import sys

INF = int(1e9)

v, e = map(int, sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())
distance = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for d in distance[1:]:
    if d != INF:
        print(d)
    else:
        print("INF")
