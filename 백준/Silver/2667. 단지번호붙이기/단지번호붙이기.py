house = []
house_cnt = 0

def dfs(x0, y0):
    global house
    global house_cnt

    if x0 < 0 or y0 < 0 or x0 >= n or y0 >= n or graph[x0][y0] != 1:
        return
    visited[x0][y0] = True
    house_cnt += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x0 + dx[i]
        ny = y0 + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] != 1:
            continue
        if not visited[nx][ny]:
            dfs(nx, ny)
    return house_cnt

n = int(input())
total = 0
graph = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        house_cnt = 0
        if graph[i][j] == 1 and not visited[i][j]:
            total += 1
            ans = dfs(i, j)
            house.append(ans)

print(total)
house.sort()
for h in house:
    print(h)
