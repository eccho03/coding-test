import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])  
    
ans = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            ans[i] += 0
        else:
            ans[i] += graph[i][j]

min_idx = ans.index(min(ans[1:]))
print(min_idx)