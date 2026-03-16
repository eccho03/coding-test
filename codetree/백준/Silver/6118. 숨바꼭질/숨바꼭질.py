from collections import deque
def bfs(start):
    q = deque()
    v = [-1]*(N+1)

    q.append(start)
    v[start]=0

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if v[nxt]==-1:
                q.append(nxt)
                v[nxt] = v[cur]+1
    return v
    # 문제에서 무조건 도달 가능하다고 제시

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]

for i, j in arr:
    graph[i].append(j)
    graph[j].append(i)

#print(graph)

dists = bfs(1)

#print(dists)
mx_dis = max(dists)
candidates = [i for i,d in enumerate(dists) if d == mx_dis]
print(min(candidates), mx_dis, len(candidates))