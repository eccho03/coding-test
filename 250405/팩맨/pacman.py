def move_mon(si, sj, dir):
    dir_cnt = 0

    #print("현재 타겟:",si,sj,dir)

    while dir_cnt < 8:
        #print(dir)
        di, dj = directions[dir]
        ni, nj = si + di, sj + dj

        if (ni, nj) != (pac_x, pac_y) and 0<=ni<4 and 0<=nj<4 and (ni, nj) not in died_monsters:
            return ni, nj, dir

        dir = (dir + 1) % 8
        dir_cnt += 1

    # 모두 움직일 수 없다면 해당 몬스터는 움직이지 x
    return si, sj, dir

def move_pack(pi, pj):
    max_cnt = -1
    best_route = None
    for i in range(4):
        for j in range(4):
            for k in range(4):
                mcnt = eat_monsters(i, j, k)
                if mcnt == -1:
                    continue
                if mcnt > max_cnt:
                    max_cnt = mcnt
                    best_route = (i, j, k)

    return best_route


def do_kill(best_route):
    global pac_x, pac_y, died_monsters

    di = [-1, 0, 1, 0]  # 상 좌 하 우
    dj = [0, -1, 0, 1]

    dir1, dir2, dir3 = best_route

    for move_dir in [dir1, dir2, dir3]:
        ni, nj = pac_x + di[move_dir], pac_y + dj[move_dir]

        # 팩맨 이동
        pac_x, pac_y = ni, nj

        # 몬스터가 있다면 죽이고, 시체 추가
        if arr[ni][nj] > 0:
            #print("죽일타겟",ni, nj)
            died_monsters.add((ni, nj))
            #print("죽은 몬스터",died_monsters)

            # 해당 칸의 몬스터 제거
            to_delete = []
            for key, (mi, mj, _) in monsters.items():
                if (mi, mj) == (ni, nj):
                    to_delete.append(key)

            for key in to_delete:
                del monsters[key]
                arr[ni][nj] -= 1  # 하나씩 차감


def eat_monsters(dir1, dir2, dir3):
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1] # 상 좌 하 우 (반시계)
    pi, pj = pac_x, pac_y
    v = [[0]*4 for _ in range(4)]

    kmon_cnt = 0 # 죽인 몬스터수

    for mov_dir in [dir1, dir2, dir3]:
        ni, nj = pi + di[mov_dir], pj + dj[mov_dir]

        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
            return -1
        if v[ni][nj] == 0:
            kmon_cnt += arr[ni][nj]
            v[ni][nj] = 1
        pi, pj = ni, nj

    return kmon_cnt

m, t = map(int, input().split())
pac_x, pac_y = map(int, input().split())
pac_x, pac_y = (pac_x-1, pac_y-1) # 좌표 조정
monsters = {} # 몬스터
monsters_idx = m
died_monsters = set() # 몬스터 시체
died_idx = 0
egg = {} # 몬스터가 낳은 알
egg_idx = 0
arr = [[0] * 4 for _ in range(4)] # 맵, 몬스터 개수 표시

# 반시계 방향
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (1, 1)]

# 초기 몬스터의 위치
for i in range(m):
    r, c, d= map(int, input().split())
    arr[r-1][c-1] = 1
    monsters[i] = (r-1, c-1, d-1)
print(arr)
#print("monsters",monsters)

# 라운드마다 아래 반복
for round in range(t):
    # print("round", round+1)
    # print("arr", arr)
    # print("monsters", monsters)
    for monster in monsters:
        # [1] 몬스터 복제 시도
        mi, mj, md = monsters[monster]
        egg[egg_idx] = (mi,mj,md)
        egg_idx += 1

        # [2] 몬스터 이동
        di, dj = directions[md]
        ni, nj = mi + di, mj + dj
        # 1)팩맨이 있는 경우 2)몬스터 시체가 있는 경우 3)격자를 벗어나는 경우 회전
        if (ni, nj) == (pac_x, pac_y) or (ni,nj) in died_monsters or ni<0 or ni>=4 or nj<0 or nj>=4:
            ni,nj,md = move_mon(mi, mj, md)
            #print("이동좌표",ni,nj,md)
            monsters[monster] = (ni, nj, md)
            arr[mi][mj] -= 1
            arr[ni][nj] += 1
        else:
            # 그렇지 않다면 한칸이동
            monsters[monster] = (ni, nj, md)
            arr[mi][mj] -= 1
            arr[ni][nj] += 1
    # print("monsters",monsters)
    # print("arr",arr)
    # print("egg",egg)

    # [3] 팩맨 이동
    #print("이동전 팩맨 좌표", pac_x, pac_y)
    best_route = move_pack(pac_x, pac_y)
    #print("best_route",best_route)
    do_kill(best_route)

    # print("monsters", monsters)
    # print("arr", arr)
    # print("egg", egg)

    # [4] 몬스터 시체 소멸
    if round % 2 == 1:
        #print("몬스터 시체 소멸")
        died_monsters.clear()

    # [5] 몬스터 복제 완성
    for i in egg:
        mi, mj, md = egg[i]
        monsters[monsters_idx] = (mi, mj, md)
        monsters_idx += 1
        arr[mi][mj] += 1 # 배열에도 몬스터 수 추가
    egg.clear() # 알이 부화했으므로 알 초기화

    #print("monsters", monsters)
    #print("arr", arr)
    #print("egg", egg)

ans = 0
# 정답 구하기 - 살아남은 몬스터 수 출력
for i in range(4):
    for j in range(4):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)
