from collections import deque
import sys

def bfs(graph, start, dis, visited):
    queue = deque([(start, 0)])
    visited[start] = True
    result = []

    while queue:
        cur, cur_dis = queue.popleft()

        if cur_dis == dis:
            result.append(cur)
            continue

        for i in graph[cur]:
            if not visited[i]:
                queue.append((i, cur_dis + 1))
                visited[i] = True
    return sorted(result)

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    graph[node1].append(node2)

visited = [False] * (n + 1)
answer = bfs(graph, x, k, visited)

print("\n".join(map(str, answer))) if answer else print("-1")