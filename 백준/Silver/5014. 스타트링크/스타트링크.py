import sys
from collections import deque

def bfs():
    queue = deque([s])
    dist[s] = 1
    
    while queue:
        node = queue.popleft()
        if node == g:
            return dist[node] - 1
        
        for i in (node + u, node - d):
            if i < 1 or i > f:
                continue
            if dist[i] == 0:
                dist[i] = dist[node] + 1
                queue.append(i)
    return "use the stairs"

f, s, g, u, d = map(int, sys.stdin.readline().split())

dist = [0] * (f + 1)

if s == g:
    print("0")
    exit()

answer = bfs()

print(answer)