import heapq

def dijkstra(start):
    pq = []
    INF = float('inf')
    dists = [INF]*(N+1)

    heapq.heappush(pq, (0, start))
    dists[start]=0

    while pq:
        cur_dis, cur_node = heapq.heappop(pq)

        if cur_dis > dists[cur_node]:
            continue

        for nxt_dis, nxt_node in graph[cur_node]:

            if nxt_dis+cur_dis < dists[nxt_node]:
                heapq.heappush(pq, (nxt_dis+cur_dis, nxt_node))
                dists[nxt_node] = nxt_dis+cur_dis

    return dists

N, M, X = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]

for start, end, time in info:
    graph[start].append([time, end]) # 도로는 단방향

# print(graph)

dist_lst = [0]*(N+1)

X_to_i = dijkstra(X)
for i in range(1, N+1):
    go_dist = dijkstra(i)   # i번 -> X번
    back_dist = X_to_i[i]

    dist_lst[i] = go_dist[X] + back_dist

print(max(dist_lst[1:]))