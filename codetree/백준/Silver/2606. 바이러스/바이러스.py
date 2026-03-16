total = 0
def dfs(graph, v, visited):
    global total
    visited[v] = True # 현재 노드 방문 처리
    for i in graph[v]:
        if not visited[i]:
            total += 1
            dfs(graph, i, visited)

computer = int(input())
cnt = int(input())
graph = [[] for _ in range(computer + 1)]
for i in range(cnt):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (computer + 1)
dfs(graph, 1, visited)
print(total)