from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]  # 북서남동

sang_size = 2  # 아기 상어 크기
eaten_cnt = 0  # 먹은 물고기 수

def grow_sang():
    global sang_size, eaten_cnt
    if eaten_cnt == sang_size:
        sang_size += 1
        eaten_cnt = 0

def loc_sang(space):
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                space[i][j] = 0
                return i, j

def target_fish(space, x, y):
    queue = deque([(x, y, 0)])
    visited = set()
    visited.add((x, y))
    fish_list = []

    while queue:
        cx, cy, dist = queue.popleft()

        # 상어보다 작은 물고기를 찾았을 때
        if 0 < space[cx][cy] < sang_size:
            fish_list.append((dist, cx, cy))

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) not in visited and space[nx][ny] <= sang_size:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))

    if fish_list:
        fish_list.sort(key=lambda x: (x[0], x[1], x[2]))  # 거리, x, y
        return fish_list[0]
    return -1, -1, -1

def bfs(x0, y0, fish_x, fish_y):
    visited = set()
    visited.add((x0, y0))
    queue = deque([(x0, y0, 0)])

    while queue:
        cx, cy, dist = queue.popleft()

        if cx == fish_x and cy == fish_y:
            return dist  # 목표 물고기까지의 거리를 반환

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) not in visited and space[nx][ny] <= sang_size:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))

    return -1  # 목표 물고기를 찾지 못했을 때

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

sang_x, sang_y = loc_sang(space)

time = 0
while True:
    dist, fish_x, fish_y = target_fish(space, sang_x, sang_y)

    if fish_x == -1:
        break

    time += dist

    space[sang_x][sang_y] = 0 # 상어 있던 자리
    sang_x, sang_y = fish_x, fish_y
    space[sang_x][sang_y] = 0 # 물고기 먹은 자리
    eaten_cnt += 1 # 먹은 물고기 수
    grow_sang() # 상어 크기 커지는지 체크

print(time)
