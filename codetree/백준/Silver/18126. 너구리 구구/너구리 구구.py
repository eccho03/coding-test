import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(cur, dist):
    global mx_dist
    v[cur]=1
    #print(cur, end=' ')

    mx_dist = max(mx_dist, dist)

    for nxt, w in graph[cur]:
        if v[nxt]==0:
            dfs(nxt, dist+w)

N = int(input())
graph = [[] for _ in range(N+1)]
mx_dist = 0
for _ in range(N-1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

v = [0]*(N+1)
dfs(1, 0)
print(mx_dist)