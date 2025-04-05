import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1),
              (1, 0), (1, 1), (0, 1), (-1, 1)]  # 반시계

dx = [-1, 0, 1, 0]  # 상좌하우
dy = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def move_mon(si, sj, dir, round):
    dir_cnt = 0
    while dir_cnt < 8:
        di, dj = directions[dir]
        ni, nj = si + di, sj + dj
        if in_range(ni, nj) and dead_body[ni][nj] <= round and (ni, nj) != (pac_x, pac_y):
            return ni, nj, dir
        dir = (dir + 1) % 8
        dir_cnt += 1
    return si, sj, dir  # 못 움직이면 제자리

def eat_monsters(d1, d2, d3):
    x, y = pac_x, pac_y
    path = []
    visited = set()
    cnt = 0
    for d in [d1, d2, d3]:
        x += dx[d]
        y += dy[d]
        if not in_range(x, y):
            return -1, []
        path.append((x, y))
    for i, j in path:
        if (i, j) not in visited:
            cnt += len(monster_map[i][j])
            visited.add((i, j))
    return cnt, path

def best_pacman_move():
    max_cnt = -1
    best_path = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                cnt, path = eat_monsters(i, j, k)
                if cnt > max_cnt or (cnt == max_cnt and path < best_path):
                    max_cnt = cnt
                    best_path = path

    return best_path

m, t = map(int, input().split())
pac_x, pac_y = map(lambda x: int(x) - 1, input().split())
monster_map = [[[] for _ in range(4)] for _ in range(4)]
dead_body = [[0] * 4 for _ in range(4)]

for _ in range(m):
    r, c, d = map(int, input().split())
    monster_map[r-1][c-1].append(d-1)

for round in range(1, t+1):
    # 1. 몬스터 복제 시도
    egg = [[list(monster_map[i][j]) for j in range(4)] for i in range(4)]

    # 2. 몬스터 이동
    new_map = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d in monster_map[i][j]:
                ni, nj, nd = move_mon(i, j, d, round)
                new_map[ni][nj].append(nd)
    monster_map = new_map

    # 3. 팩맨 이동
    path = best_pacman_move()
    for x, y in path:
        if monster_map[x][y]:
            monster_map[x][y] = []
            dead_body[x][y] = round + 2
    if path:
        pac_x, pac_y = path[-1]

    # 4. 몬스터 시체 소멸
    for i in range(4):
        for j in range(4):
            if dead_body[i][j] == round:
                dead_body[i][j] = 0

    # 5. 몬스터 복제 완성
    for i in range(4):
        for j in range(4):
            monster_map[i][j].extend(egg[i][j])

# 최종 몬스터 수 세기
ans = 0
for i in range(4):
    for j in range(4):
        ans += len(monster_map[i][j])
print(ans)
