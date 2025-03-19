from collections import deque


def bfs(x0, y0, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x0, y0)])
    country = deque([(x0, y0)])
    visited.add((x0, y0))
    total = graph[x0][y0]

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not (nx, ny) in visited and L <= abs(graph[cx][cy] - graph[nx][ny]) <= R:
                    q.append((nx, ny))
                    country.append((nx, ny))
                    visited.add((nx, ny))
                    total += graph[nx][ny]

    return country, total


N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

days = 0

while True:
    visited = set()
    is_moved = False

    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                country, total_people = bfs(i, j, visited)

                if len(country) > 1:
                    is_moved = True
                    new_people = total_people // len(country)
                    for x, y in country:
                        graph[x][y] = new_people
    if not is_moved:
        break
    days += 1
print(days)