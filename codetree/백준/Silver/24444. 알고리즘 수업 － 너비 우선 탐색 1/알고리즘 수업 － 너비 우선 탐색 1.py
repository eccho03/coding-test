import sys
from collections import deque

def bfs(start, visited, order):
    queue = deque([start])
    visited[start] = True
    index = 1
    order[start] = index
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                index += 1
                order[i] = index

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for edges in graph:
    edges.sort()

visited = [False] * (n + 1)
order = [0] * (n + 1)

bfs(r, visited, order)

sys.stdout.write("\n".join(map(str, order[1:])) + "\n")