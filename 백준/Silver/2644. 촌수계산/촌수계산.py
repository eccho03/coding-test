chon = -1
def dfs(v, cnt):
    global chon
    visited[v] = True
    if v == num2:
        chon = cnt
        return

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt + 1)

n = int(input())
num1, num2 = map(int, input().split())
m = int(input())

# 번호 1부터 시작
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(num1, 0)
print(chon)
