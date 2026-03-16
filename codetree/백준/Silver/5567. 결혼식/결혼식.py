import sys
from collections import deque

def bfs(start, visited):
    queue = deque([(start, 0)])
    visited[start] = True
    ans = 0

    while queue:
        v, relation = queue.popleft()
        if (relation == 1 or relation == 2):
            ans += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, relation + 1))
    return ans


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
ans = bfs(1, visited)
print(ans)