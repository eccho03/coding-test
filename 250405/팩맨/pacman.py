import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = 4
dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 반시계 45도
dy = [0, -1, -1, -1, 0, 1, 1, 1]
pdx = [-1, 0, 1, 0]  # 상좌하우
pdy = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def monster_make_egg():
    return [m[:] for m in m_arr]

def monster_move(rounds):
    new_m_arr = []
    for mx, my, md in m_arr:
        for i in range(8):
            nd = (md + i) % 8
            nx, ny = mx + dx[nd], my + dy[nd]
            if in_range(nx, ny) and dead_body[nx][ny] == 0 and not (nx == px and ny == py):
                new_m_arr.append([nx, ny, nd])
                break
        else:
            new_m_arr.append([mx, my, md])
    return new_m_arr

def eat_monster(i, j, z):
    path = []
    visited = set()
    eat = 0
    nx, ny = px, py
    for d in [i, j, z]:
        nx += pdx[d]
        ny += pdy[d]
        if not in_range(nx, ny):
            return -1, []
        path.append((nx, ny))
    for x, y in set(path):
        eat += sum(1 for mx, my, _ in m_arr if mx == x and my == y)
    return eat, path

def pacman_move(rounds):
    global px, py, m_arr
    max_eat = -1
    best_path = []
    best_dirs = ()
    for i in range(4):
        for j in range(4):
            for z in range(4):
                eat, path = eat_monster(i, j, z)
                if eat > max_eat or (eat == max_eat and path < best_path):
                    max_eat = eat
                    best_path = path
                    best_dirs = (i, j, z)
    if not best_path:
        return
    # 몬스터 제거 + 시체 남기기
    new_m_arr = []
    for mx, my, md in m_arr:
        if (mx, my) not in best_path:
            new_m_arr.append([mx, my, md])
        else:
            dead_body[mx][my] = 3  # 시체는 2턴 후 사라지므로 3으로 설정
    m_arr = new_m_arr
    # 팩맨 이동
    for d in best_dirs:
        px += pdx[d]
        py += pdy[d]

def dead_body_decay():
    for i in range(n):
        for j in range(n):
            if dead_body[i][j] > 0:
                dead_body[i][j] -= 1

def egg_up(eggs):
    for ex, ey, ed in eggs:
        m_arr.append([ex, ey, ed])

def count_monsters():
    return len(m_arr)

# 입력
m, t = map(int, input().split())
px, py = map(lambda x: int(x)-1, input().split())
m_arr = [list(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
dead_body = [[0]*n for _ in range(n)]

# 시뮬레이션
for round in range(t):
    eggs = monster_make_egg()       # 1. 알 복제
    m_arr = monster_move(round)     # 2. 몬스터 이동
    pacman_move(round)              # 3. 팩맨 이동 및 시체 생성
    dead_body_decay()               # 4. 시체 감소
    egg_up(eggs)                    # 5. 알 부화

# 결과 출력
print(count_monsters())
