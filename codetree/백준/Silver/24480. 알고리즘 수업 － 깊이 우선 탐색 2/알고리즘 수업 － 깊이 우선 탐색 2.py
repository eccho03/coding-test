import sys

sys.setrecursionlimit(10**6)

idx = 0
def dfs(v):
    global idx
    global result
    idx += 1
    result[v] = idx
    
    visited[v] = True
    graph[v].sort(reverse=True)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return False

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for i in range(1, n + 1):
    print(result[i])