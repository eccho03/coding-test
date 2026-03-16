from collections import deque
def bfs(start):
    q = deque()
    v = [0] * (N+1)
    order = [0] * (N+1)

    q.append(start)
    v[start]=1
    tmp = 1

    while q:
        cur = q.popleft()
        order[cur] = tmp
        tmp+=1

        # print(cur)

        for nxt in graph[cur]:
            if v[nxt]==0:
                q.append(nxt)
                v[nxt]=1

    return order


N, M, R = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
graph =[[] for _ in range(N+1)]

info.sort(reverse=True)

for u, v in info:
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
order = bfs(R)

for i in order[1:]:
    print(i)