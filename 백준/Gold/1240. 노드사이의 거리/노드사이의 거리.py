import sys
sys.setrecursionlimit(10**4)
def dfs(start, end, dist):
    v[start]=1
    #print(start, dist)
    if start == end:
        print(dist)
        return

    #print(graph[start])

    for i in graph[start]:
        cur, cur_dist = i[0], i[1]
        #print(cur, cur_dist)
        if v[cur]==0:
            dfs(cur, end, cur_dist+dist)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

#print(graph)
for _ in range(M):
    a, b = map(int, input().split())
    v = [0]*(N+1)
    dfs(a, b, 0)
    #print(a, b)
