import sys
from collections import deque

def bfs(start, dis):
    queue = deque([(start, 0)])

    visited[start] = True
    result = []

    while queue:
        cur_node, cur_dis = queue.popleft()

        if cur_dis == dis:
            result.append(cur_node)
            continue
        
        for i in graph[cur_node]:
            if not visited[i]:
                queue.append((i, cur_dis + 1))
                visited[i] = True
    return sorted(result)

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

answer = bfs(x, k)

if len(answer) == 0:
    print("-1")
else:
    for i in answer:
        print(i)