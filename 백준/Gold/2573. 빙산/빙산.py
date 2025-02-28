from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_bingha():
    return [[graph[i][j] != 0 for j in range(m)] for i in range(n)]

def count_bingha():
    visited = [[False] * m for _ in range(n)]
    num_bingha = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                num_bingha += 1
                if num_bingha > 1:
                    return num_bingha
    return num_bingha

def melt_bingha():
    melt_cnt = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                ocean_cnt = 0
                for d  in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if ni < 0 or nj < 0 or ni >= n or nj >= m:
                        continue
                    if graph[ni][nj] == 0:
                        ocean_cnt += 1
                melt_cnt[i][j] = ocean_cnt

    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - melt_cnt[i][j])

def bfs(x0, y0, visited):
    queue = deque([(x0, y0)])
    visited[x0][y0] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

year = 0

while True:

    num_bingha = count_bingha()

    if num_bingha == 0:
        print(0)
        break
    elif num_bingha >= 2:
        print(year)
        break
    
    melt_bingha()
    year += 1