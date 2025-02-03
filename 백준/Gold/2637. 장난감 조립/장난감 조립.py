import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

indegree = [0] * (n + 1)
basic = []
graph = [[] for _ in range(n + 1)]
basic_num =[[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append((y, k))
    indegree[y] += 1

for i in range(1, n):
    if not graph[i]: 
        basic.append(i)

def topology():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            basic_num[i][i] = 1
    while q:
        now = q.popleft()
       
        for next, k in graph[now]:
            for i in range(1, n + 1):
                basic_num[next][i] += basic_num[now][i] * k
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    for i in range(1, n + 1):
        if i in basic:
            print(i, basic_num[i][n])   

topology()