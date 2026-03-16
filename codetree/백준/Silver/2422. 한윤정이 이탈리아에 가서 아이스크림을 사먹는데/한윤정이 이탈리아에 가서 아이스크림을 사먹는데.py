N, M = map(int, input().split())
bad = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]

for a, b in bad:
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

ans = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        # print(i, j)
        # print(graph[i], j)
        if j not in graph[i] and i not in graph[j]:
            for k in range(j+1, N+1):
                if k not in graph[j] and j not in graph[k] and i not in graph[k] and k not in graph[i]:
                    ans += 1
                    # print(i, j, k)
print(ans)