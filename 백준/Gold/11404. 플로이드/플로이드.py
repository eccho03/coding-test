import sys

INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])  
    

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print("")
