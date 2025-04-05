from collections import deque
def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n,m,v = map(int,input().split())

visited = [False] * (n+1)
graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for edge in graph:
    edge.sort()
    
dfs(v)
visited = [False] * (n+1)
print("")
bfs(v)