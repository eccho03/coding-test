N, M, K = map(int, input().split())
arr = [[10] * (N+2)] + [[10]+list(map(int, input().split()))+[10] for _ in range(N)]+[[10] * (N+2)]
players = [tuple(map(int, input().split())) for _ in range(M)]
exit_x, exit_y = map(int, input().split())

ans = 0

# 거리 계산
def dist(x, y):
    return abs(x - exit_x) + abs(y - exit_y)

# 가장 가까운 생존자 포함 정사각형 좌상단 좌표, 길이 구하기
def find_square():
    min_d = float('inf')
    min_x = min_y = l = -1
    for x, y in players:
        d = dist(x, y)
        if d < min_d:
            min_d = d

    # 최소 거리의 생존자 중 가장 작은 정사각형 찾기
    for size in range(1, N+1):
        for i in range(1, N - size + 2):
            for j in range(1, N - size + 2):
                if not (i <= exit_x <= i+size-1 and j <= exit_y <= j+size-1):
                    continue
                for px, py in players:
                    if dist(px, py) == min_d and (i <= px <= i+size-1 and j <= py <= j+size-1):
                        return i, j, size
    return -1, -1, -1

# 정사각형 회전
def rotate(sx, sy, L):
    global arr, exit_x, exit_y, players
    temp = [[0]*L for _ in range(L)]
    for i in range(L):
        for j in range(L):
            temp[j][L-1-i] = arr[sx+i][sy+j]

    for i in range(L):
        for j in range(L):
            arr[sx+i][sy+j] = temp[i][j]
            if arr[sx+i][sy+j] > 0:
                arr[sx+i][sy+j] -= 1

    # 출구 회전
    if sx <= exit_x <= sx+L-1 and sy <= exit_y <= sy+L-1:
        ox, oy = exit_x - sx, exit_y - sy
        exit_x = sx + oy
        exit_y = sy + (L - 1 - ox)

    # 생존자 회전
    new_players = []
    for x, y in players:
        if sx <= x <= sx+L-1 and sy <= y <= sy+L-1:
            ox, oy = x - sx, y - sy
            nx = sx + oy
            ny = sy + (L - 1 - ox)
            new_players.append((nx, ny))
        else:
            new_players.append((x, y))
    players = new_players

for _ in range(K):
    # [1] 생존자 이동
    new_players = []
    for x, y in players:
        if (x, y) == (exit_x, exit_y):
            continue
        moved = False
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + di, y + dj
            if arr[nx][ny] == 0 and dist(nx, ny) < dist(x, y):
                new_players.append((nx, ny))
                ans += 1
                moved = True
                break
        if not moved:
            new_players.append((x, y))
    players = new_players

    # 모두 탈출했는지 확인
    players = [p for p in players if p != (exit_x, exit_y)]
    if not players:
        break

    # 가장 가까운 생존자 포함 최소 정사각형 회전
    sx, sy, l = find_square()
    if sx != -1:
        rotate(sx, sy, l)

print(ans)
print(exit_x, exit_y)
