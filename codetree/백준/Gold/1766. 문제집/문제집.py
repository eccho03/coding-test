import heapq
def topology_sort():
    result = []
    pq = []

    for i in range(1, N+1):
        if indegree[i]==0:
            heapq.heappush(pq, i)

    while pq:
        cur = heapq.heappop(pq)
        result.append(cur)
        for i in graph[cur]:
            indegree[i]-=1
            if indegree[i]==0:
                heapq.heappush(pq, i)


    for i in result:
        print(i, end=" ")

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for first, second in info:
    graph[first].append(second)
    indegree[second]+=1

topology_sort()
