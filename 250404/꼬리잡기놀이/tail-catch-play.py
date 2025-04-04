from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 하 좌

def bfs(si, sj, team_idx):
    q = deque([(si, sj)])
    v = set()
    v.add((si, sj))
    team = deque()
    team.append((si, sj))
    arr[si][sj] = team_idx

    while q:
        ci, cj = q.popleft()
        for d in directions:
            ni, nj = ci + d[0], cj + d[1]
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in v:
                if arr[ni][nj] == 2 or (arr[ni][nj] == 3 and (ci, cj) != (si, sj)):
                    v.add((ni, nj))
                    q.append((ni, nj))
                    team.append((ni, nj))
                    arr[ni][nj] = team_idx
    return team

def move():
    for t_idx in teams:
        dq = teams[t_idx]
        tail_i, tail_j = dq.pop()
        arr[tail_i][tail_j] = 4  # 이동선
        head_i, head_j = dq[0]
        for d in directions:
            ni, nj = head_i + d[0], head_j + d[1]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 4:
                dq.appendleft((ni, nj))
                arr[ni][nj] = t_idx
                break

def ball_throw(round):
    direction = (round // n) % 4
    offset = round % n

    if direction == 0:  # 오른쪽
        for j in range(n):
            if arr[offset][j] >= 5:
                return (offset, j)
    elif direction == 1:  # 위쪽
        for i in reversed(range(n)):
            if arr[i][offset] >= 5:
                return (i, offset)
    elif direction == 2:  # 왼쪽
        for j in reversed(range(n)):
            if arr[n - 1 - offset][j] >= 5:
                return (n - 1 - offset, j)
    else:  # 아래쪽
        for i in range(n):
            if arr[i][n - 1 - offset] >= 5:
                return (i, n - 1 - offset)
    return (-1, -1)

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 팀 구성
teams = {}
team_idx = 5
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            teams[team_idx] = bfs(i, j, team_idx)
            team_idx += 1

ans = 0
for round in range(k):
    move()
    ci, cj = ball_throw(round)
    if ci == -1:  # 아무도 안 맞음
        continue
    team_id = arr[ci][cj]
    idx = teams[team_id].index((ci, cj))
    ans += (idx + 1) ** 2
    teams[team_id] = deque(reversed(teams[team_id]))

print(ans)
