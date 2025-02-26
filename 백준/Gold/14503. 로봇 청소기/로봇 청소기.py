from collections import deque

answer = 0

def turn_90(direct):
    return (direct + 3) % 4

def bfs(x0, y0, direct):
    global answer
    queue = deque([(x0, y0)])
    visited[x0][y0] = True
    answer += 1

    dx = [-1, 0, 1, 0] # 남북
    dy = [0, 1, 0, -1] # 서동

    while queue:
        x, y = queue.popleft()
        cleaned = False

        for _ in range(4):
            direct = turn_90(direct)
            nx, ny = x + dx[direct], y + dy[direct]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                answer += 1
                cleaned = True
                break

        if not cleaned:
            back_x, back_y = x - dx[direct], y - dy[direct]
            if graph[back_x][back_y] == 0:
                queue.append((back_x, back_y))
            else:
                return answer
    return answer

n, m = map(int, input().split())

# 처음 로봇 청소기 좌표 / 방향
r, c, d = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

print(bfs(r, c, d))