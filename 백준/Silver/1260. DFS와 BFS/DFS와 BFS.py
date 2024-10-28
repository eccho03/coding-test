from collections import deque

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드 방문 처리
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)  
    graph[node2].append(node1)

for edges in graph:
    edges.sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print("")
visited = [False] * (n + 1)
bfs(graph, v, visited)
