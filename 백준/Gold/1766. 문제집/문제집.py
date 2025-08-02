from collections import deque
def topology_sort():
    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        q = deque(q)
        cur = q.popleft()
        result.append(cur)
        for i in graph[cur]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

        q = sorted(q)

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
