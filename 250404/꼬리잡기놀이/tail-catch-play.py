import sys
from collections import deque
input = sys.stdin.readline

# 방향: 상우하좌
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

teams = {}
team_n = 5  # 팀 번호는 5번부터 사용
v = [[0] * n for _ in range(n)]

# [1] BFS로 팀 구성원 좌표 저장 및 팀 번호 매기기
def bfs(si, sj, team_n):
    q = deque()
    team = deque()

    q.append((si, sj))
    v[si][sj] = 1
    team.append((si, sj))
    arr[si][sj] = team_n

    while q:
        ci, cj = q.popleft()
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0:
                if arr[ni][nj] == 2 or (arr[ni][nj] == 3 and (ci, cj) != (si, sj)):
                    v[ni][nj] = 1
                    q.append((ni, nj))
                    team.append((ni, nj))
                    arr[ni][nj] = team_n
    teams[team_n] = team

# 팀별 구성 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0:
            bfs(i, j, team_n)
            team_n += 1

# 방향 순서: 우 → 상 → 좌 → 하
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
ans = 0

# [2] 매 라운드마다 이동 + 공 던지기
for r in range(k):
    # [2-1] 각 팀 이동
    for t in teams.values():
        tail_i, tail_j = t.pop()  # 꼬리 제거
        arr[tail_i][tail_j] = 4   # 이동선 복원

        head_i, head_j = t[0]     # 머리 위치
        for d in range(4):
            ni, nj = head_i + di[d], head_j + dj[d]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 4:
                t.appendleft((ni, nj))
                arr[ni][nj] = arr[head_i][head_j]  # 팀 번호로 덮어쓰기
                break

    # [2-2] 공 던지기 방향 계산
    d = (r // n) % 4
    offset = r % n
    if d == 0:
        ci, cj = offset, 0
    elif d == 1:
        ci, cj = n - 1, offset
    elif d == 2:
        ci, cj = n - 1 - offset, n - 1
    else:
        ci, cj = 0, n - 1 - offset

    # [2-3] 공이 사람을 맞추면 점수 획득
    for _ in range(n):
        if 0 <= ci < n and 0 <= cj < n and arr[ci][cj] >= 5:
            team_id = arr[ci][cj]
            team = teams[team_id]
            idx = team.index((ci, cj))
            ans += (idx + 1) ** 2
            team.reverse()  # 머리-꼬리 반전
            break
        ci += di[d]
        cj += dj[d]

print(ans)
