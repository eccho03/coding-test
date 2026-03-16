import sys
sys.setrecursionlimit(10**9)

def dfs(num, d):
    global order
    # print(num, depth, end=' ')
    depth[num] = d
    v[num]=order

    graph[num].sort() #정점번호 오름차순 방문
    for i in graph[num]:
        if v[i]==0:
            order+=1
            dfs(i, d+1)

N, M, R = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]

for u, v in info:
    graph[u].append(v)
    graph[v].append(u)

v = [0]*(N+1)
depth = [-1]*(N+1)
# print(graph)
ans = 0
order = 1

dfs(R, 0)

for i in range(1, N+1):
    if depth[i]!=-1:
        ans += depth[i]*v[i]

print(ans)