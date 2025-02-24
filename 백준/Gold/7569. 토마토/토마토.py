from collections import deque

queue = deque()

def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    global deque

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

m, n, h = map(int, input().split())
graph = [[[0] * m for _ in range(n)] for _ in range(h)]

for z in range(h):
    for x in range(n):
        graph[z][x] = list(map(int, input().split()))
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append((z, x, y))
bfs()

answer = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                print("-1")
                exit()
            answer = max(answer, graph[z][x][y])

print(answer-1)