
def find_air():
    # 공기청정기의 위치 반환
    air_loc = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                air_loc.append((i, j))
    return air_loc

def dust_plus():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    spread = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1 and graph[i][j] != 0:
                spread[i][j] = graph[i][j] // 5
    # print(spread)

    for cx in range(r):
        for cy in range(c):

            if graph[cx][cy] > 0:
                spread_cnt = 0
                spread_mount = spread[cx][cy]

                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == -1:
                        continue

                    if spread_mount > 0:
                        spread_cnt += 1
                        graph[nx][ny] += spread_mount
                graph[cx][cy] -= spread_cnt * spread_mount

def shift_counterclockwise(air):
    ax, ay = air[0]

    # 위쪽 이동 - 따로 복사본 만들어서 진행
    new_graph = [row[:] for row in graph]

    # 1. 왼쪽으로 당기기
    for i in range(ax - 1, 0, -1):
        new_graph[i][0] = graph[i - 1][0]

    # 2. 위쪽으로 당기기
    for i in range(c - 1):
        new_graph[0][i] = graph[0][i + 1]

    # 3. 오른쪽으로 당기기
    for i in range(ax):
        new_graph[i][c - 1] = graph[i + 1][c - 1]

    # 4. 아래쪽으로 당기기
    for i in range(c - 1, 1, -1):
        new_graph[ax][i] = graph[ax][i - 1]

    new_graph[ax][1] = 0  # 공기청정기에서 나오는 공기

    # 적용
    for i in range(ax + 1):
        graph[i] = new_graph[i]


def shift_clockwise(air):
    ax, ay = air[1]

    # 아래쪽 이동 - 따로 복사본 만들어서 진행
    new_graph = [row[:] for row in graph]

    # 1. 왼쪽으로 당기기
    for i in range(ax + 1, r - 1):
        new_graph[i][0] = graph[i + 1][0]

    # 2. 아래쪽으로 당기기
    for i in range(c - 1):
        new_graph[r - 1][i] = graph[r - 1][i + 1]

    # 3. 오른쪽으로 당기기
    for i in range(r - 1, ax, -1):
        new_graph[i][c - 1] = graph[i - 1][c - 1]

    # 4. 위쪽으로 당기기
    for i in range(c - 1, 1, -1):
        new_graph[ax][i] = graph[ax][i - 1]

    new_graph[ax][1] = 0  # 공기청정기에서 나오는 공기

    # 적용
    for i in range(ax, r):
        graph[i] = new_graph[i]

r, c, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]

for i in range(t): # t초 동안 반복
    air = find_air()
    # print(air)

    # 미세먼지 확산
    dust_plus()

    # print("미세먼지확산",graph)

    shift_counterclockwise(air)
    shift_clockwise(air)

    # print(graph)
print(sum(sum(row) for row in graph) + 2)  # 공기청정기(-1) 두 개 있으니까 +2
    # 공기청정기 작동()
# dust = cnt_dust()
# print(dust)