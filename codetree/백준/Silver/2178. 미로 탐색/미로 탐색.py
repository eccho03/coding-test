from collections import deque

def bfs(x0, y0, xn, yn):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x0, y0)])
    visited[x0][y0] = True
    distance[x0][y0] = 1

    while queue:
        x, y = queue.popleft()

        if x == xn and y == yn:
            return distance[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and miro[nx][ny] == 1: # 이동할 수 있는 칸일 때만
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())

miro = []
for _ in range(n):
    arr = list(map(int, input()))
    miro.append(arr)

visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

answer = bfs(0, 0, n - 1, m - 1) 
print(answer)