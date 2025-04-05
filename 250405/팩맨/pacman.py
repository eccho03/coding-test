def move_pack(si, sj, dir):
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
    return -1,-1,-1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1] # 상 좌 하 우
dir_order = ['u','l','d','r']
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
                # 이미 방문했어도 이동은 가능, 하지만 몬스터는 먹지 않아야 함
                dfs(ni, nj, n + 1, mcnt, path + [(ni, nj)], visited)

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

max_monsters = -1

# 반시계 방향
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (1, 1)]

# 초기 몬스터의 위치
for i in range(m):
    r, c, d= map(int, input().split())
    arr[r-1][c-1] = 1
    monsters[i] = (r-1, c-1, d-1)
#print(arr)
#print("monsters",monsters)

# 라운드마다 아래 반복
for round in range(t):
    max_monsters = -1
    best_path = []
    for monster in sorted(list(monsters.keys())):
        # [1] 몬스터 복제 시도
        mi, mj, md = monsters[monster]
        egg[egg_idx] = (mi,mj,md)
        egg_idx += 1

        # [2] 몬스터 이동
        di, dj = directions[md]
        ni, nj = mi + di, mj + dj
        # 1)팩맨이 있는 경우 2)몬스터 시체가 있는 경우 3)격자를 벗어나는 경우 회전
        if (ni, nj) == (pac_x, pac_y) or (ni,nj) in died_monsters or ni<0 or ni>=4 or nj<0 or nj>=4:
            ni,nj,md = move_pack(mi, mj, md)
            #print("이동좌표",ni,nj,md)
            if ni != -1:
                monsters[monster] = (ni, nj, md)
                arr[mi][mj] -= 1
                arr[ni][nj] += 1
        else:
            # 그렇지 않다면 한칸이동
            monsters[monster] = (ni, nj, md)
            arr[mi][mj] -= 1
            arr[ni][nj] += 1
    #print("monsters",monsters)
    #print("arr",arr)
    #print("egg",egg)

    # [3] 팩맨 이동
    #print("이동전 팩맨 좌표", pac_x, pac_y)
    dfs(pac_x, pac_y, 0, 0, [], set())

    # 팩맨이 몬스터 잡는 부분 수정
    if best_path:
        pac_x, pac_y = best_path[-1]

        # 잡은 몬스터 수 계산 및 시체 표시
        for x, y in best_path:
            if arr[x][y] > 0:
                max_monsters += arr[x][y]
                died_monsters.add((x, y))
                arr[x][y] = 0

        to_remove = []
        for idx in list(monsters.keys()):
            mi, mj, _ = monsters[idx]
            if (mi, mj) in best_path:
                to_remove.append(idx)
        for idx in to_remove:
            arr[monsters[idx][0]][monsters[idx][1]] -= 1
            del monsters[idx]

    eaten_set = set()
    for x, y in best_path:
        if arr[x][y] > 0:
            died_monsters.add((x, y))
            arr[x][y] = 0

    #print("after pack mon", monsters)
    #print("after pack arr",arr)

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
    #print("몬스터 복제 완성",monsters)
    #print("몬스터 복제후배열", arr)
    egg.clear()

ans = 0
# 정답 구하기 - 살아남은 몬스터 수 출력
for i in range(4):
    for j in range(4):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)
