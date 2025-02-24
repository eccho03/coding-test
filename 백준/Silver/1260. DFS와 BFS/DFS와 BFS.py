import sys
from collections import deque
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for edge in graph:
    edge.sort()
    
dfs(v)

visited = [False] * (n + 1)
print("")

bfs(v)