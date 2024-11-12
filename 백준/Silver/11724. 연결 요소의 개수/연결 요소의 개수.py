import sys
sys.setrecursionlimit(10**6)

def dfs(v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if (visited[i] == True):
        continue
    dfs(i, visited)
    cnt += 1
print(cnt)