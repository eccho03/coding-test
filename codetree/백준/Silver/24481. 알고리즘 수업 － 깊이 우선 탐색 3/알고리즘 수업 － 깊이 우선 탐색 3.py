import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(num, depth):
    v[num] = 1
    depths[num] = depth

    graph[num].sort() #정점번호 오름차순 방문
    for i in graph[num]:
        if v[i]==0:
            dfs(i, depth+1)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

v = [0]*(N+1)
depths = [-1]*(N+1)
dfs(R, 0)
for i in range(1, N+1):
    print(depths[i])