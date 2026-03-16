import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]: 
            res[i] = v
            dfs(i)
arr = []
n = int(input())
res = [0] * (n + 1)
visited = [False] * (n + 1) 
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs(1)
for i in range(2, n + 1):
    print(res[i])
