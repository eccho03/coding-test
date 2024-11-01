res = -1
def dfs(v, cnt):
    global res
    visited[v] = True
    if v == p2:
        res = cnt
        return
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt + 1)

total = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(total + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (total + 1)
dfs(p1, 0)
print(res)
