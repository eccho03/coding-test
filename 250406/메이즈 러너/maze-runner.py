import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[10] * (N + 2)] + [[10] + list(map(int, input().split())) + [10] for _ in range(N)] + [[10] * (N + 2)]
players = [tuple(map(int, input().split())) for _ in range(M)]
exit_x, exit_y = map(int, input().split())

ans = 0

def dist(x, y):
    return abs(x - exit_x) + abs(y - exit_y)

# 가장 가까운 생존자가 포함된 가장 작은 정사각형 찾기
def find_square():
    min_d = float('inf')
    cand = []

    for x, y in players:
        d = dist(x, y)
        if d < min_d:
            min_d = d
            cand = [(x, y)]
        elif d == min_d:
            cand.append((x, y))

    cand.sort()  # 위 -> 왼쪽 우선

    for size in range(1, N + 1):
        for i in range(1, N - size + 2):
            for j in range(1, N - size + 2):
                if not (i <= exit_x <= i + size - 1 and j <= exit_y <= j + size - 1):
                    continue
                for cx, cy in cand:
                    if i <= cx <= i + size - 1 and j <= cy <= j + size - 1:
                        return i, j, size
    return -1, -1, -1

def rotate(sx, sy, L):
    global arr, exit_x, exit_y, players
    temp = [[0] * L for _ in range(L)]

    for i in range(L):
        for j in range(L):
            temp[j][L - 1 - i] = arr[sx + i][sy + j]

    for i in range(L):
        for j in range(L):
            arr[sx + i][sy + j] = temp[i][j]
            if arr[sx + i][sy + j] > 0:
                arr[sx + i][sy + j] -= 1

    # 출구 좌표 회전
    if sx <= exit_x <= sx + L - 1 and sy <= exit_y <= sy + L - 1:
        ox, oy = exit_x - sx, exit_y - sy
        exit_x = sx + oy
        exit_y = sy + (L - 1 - ox)

    # 생존자 회전
    new_players = []
    for x, y in players:
        if sx <= x <= sx + L - 1 and sy <= y <= sy + L - 1:
            ox, oy = x - sx, y - sy
            nx = sx + oy
            ny = sy + (L - 1 - ox)
            new_players.append((nx, ny))
        else:
            new_players.append((x, y))
    players = new_players

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    # [1] 생존자 이동
    new_players = []
    for x, y in players:
        moved = False
        for d in range(4):  # 상하좌우 우선순위
            nx = x + dx[d]
            ny = y + dy[d]
            if arr[nx][ny] == 0 and dist(nx, ny) < dist(x, y):
                new_players.append((nx, ny))
                ans += 1
                moved = True
                break
        if not moved:
            new_players.append((x, y))
    players = new_players

    # [2] 이동 후 즉시 탈출 처리
    players = [p for p in players if p != (exit_x, exit_y)]
    if not players:
        break

    # [3] 회전
    sx, sy, l = find_square()
    if sx != -1:
        rotate(sx, sy, l)

print(ans)
print(exit_x, exit_y)
