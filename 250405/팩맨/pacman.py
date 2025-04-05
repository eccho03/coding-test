import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def move_pack(si, sj, dir):
    dir_cnt = 0
    while dir_cnt < 8:
        di, dj = directions[dir]
        ni, nj = si + di, sj + dj

        if (ni, nj) != (pac_x, pac_y) and 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) not in died_monsters:
            return ni, nj, dir

        dir = (dir + 1) % 8
        dir_cnt += 1

    return -1, -1, -1

dx = [-1, 0, 1, 0]  # 상 좌 하 우
dy = [0, -1, 0, 1]
best_path = []

def dfs(pi, pj, n, mcnt, path, visited):
    global max_monsters, best_path

    if n == 3:
        if mcnt > max_monsters:
            max_monsters = mcnt
            best_path = path[:]
        return

    for i in range(4):
        ni, nj = pi + dx[i], pj + dy[i]
        if 0 <= ni < 4 and 0 <= nj < 4:
            if (ni, nj) not in visited:
                visited.add((ni, nj))
                plus = arr[ni][nj]
                dfs(ni, nj, n + 1, mcnt + plus, path + [(ni, nj)], visited)
                visited.remove((ni, nj))
            else:
                dfs(ni, nj, n + 1, mcnt, path + [(ni, nj)], visited)

m, t = map(int, input().split())
pac_x, pac_y = map(int, input().split())
pac_x, pac_y = (pac_x - 1, pac_y - 1)

monsters = {}
monsters_idx = m
died_monsters = set()
egg = {}
arr = [[0] * 4 for _ in range(4)]

max_monsters = -1

# 반시계 방향
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1),
              (1, 0), (1, 1), (0, 1), (-1, 1)]

# 초기 몬스터 정보 입력
for i in range(m):
    r, c, d = map(int, input().split())
    arr[r - 1][c - 1] += 1
    monsters[i] = (r - 1, c - 1, d - 1)

# t 라운드 진행
for round in range(t):
    max_monsters = -1
    best_path = []

    # 1. 몬스터 복제 시도 (알 저장)
    egg.clear()
    for idx, (mi, mj, md) in monsters.items():
        egg[idx] = (mi, mj, md)

    # 2. 몬스터 이동
    new_monsters = {}
    new_arr = [[0] * 4 for _ in range(4)]
    for idx, (mi, mj, md) in monsters.items():
        ni, nj, nd = move_pack(mi, mj, md)
        if ni != -1:
            new_monsters[idx] = (ni, nj, nd)
            new_arr[ni][nj] += 1
        else:
            new_monsters[idx] = (mi, mj, md)
            new_arr[mi][mj] += 1
    monsters = new_monsters
    arr = new_arr

    # 3. 팩맨 이동 및 몬스터 제거
    dfs(pac_x, pac_y, 0, 0, [], set())
    if best_path:
        pac_x, pac_y = best_path[-1]
        remove_idx = []
        for x, y in best_path:
            if arr[x][y] > 0:
                arr[x][y] = 0
                died_monsters.add((x, y))
        for idx, (mi, mj, _) in list(monsters.items()):
            if (mi, mj) in best_path:
                remove_idx.append(idx)
        for idx in remove_idx:
            del monsters[idx]

    # 4. 몬스터 시체 소멸 (2턴 주기)
    if round % 2 == 1:
        died_monsters.clear()

    # 5. 몬스터 복제 완성
    for ei in egg:
        mi, mj, md = egg[ei]
        monsters[monsters_idx] = (mi, mj, md)
        arr[mi][mj] += 1
        monsters_idx += 1

# 정답 출력
ans = 0
for i in range(4):
    for j in range(4):
        ans += arr[i][j]
print(ans)
