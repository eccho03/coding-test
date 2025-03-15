from copy import deepcopy
from collections import deque

directions = {
    1: [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],  # 한 방향
    2: [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],  # 두 방향
    3: [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)]],  # 직각
    4: [[(-1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, -1)], [(1, 0), (0, -1), (0, 1)]],  # 3방향
    5: [[(-1, 0), (1, 0), (0, -1), (0, 1)]]  # 4방향
}

n, m = map(int, input().split())
cctvs = []
space = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))
    space.append(row)

def check_area(tmp_space, x, y, dirs):
    for dx, dy in dirs:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy

            if not (0 <= nx < n and 0 <= ny < m) or tmp_space[nx][ny] == 6:
                break
            if tmp_space[nx][ny] == 0:
                tmp_space[nx][ny] = "#"

ans = float('inf')
def dfs(depth, space):
    global ans
    if depth == len(cctvs):
        cnt = sum(row.count(0) for row in space)
        ans = min(ans, cnt)
        return

    x, y, cctv_type = cctvs[depth]

    for dir in directions[cctv_type]:
        tmp_space = deepcopy(space)
        check_area(tmp_space, x, y, dir)
        dfs(depth + 1, tmp_space)

dfs(0, space)

print(ans)