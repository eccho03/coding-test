import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 하 좌

def head_team():
    team = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                team.append((i, j))

    return team

def bfs(si, sj):
    q = deque([(si, sj)])
    v = set()
    v.add((si, sj))

    mate = [(si, sj)]

    while q:
        ci, cj = q.popleft()

        for i in directions:
            ni, nj = ci + i[0], cj + i[1]

            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue

            if (ni, nj) not in v:
                # 꼬리 사람일 경우 한 바퀴 도는 경우 제외
                if arr[ni][nj] == 2 or (arr[ni][nj] == 3 and (ci, cj)!=(si, sj)):
                    # 중간 사람이나 꼬리 사람이라면
                    v.add((ni, nj))
                    q.append((ni, nj))
                    mate.append((ni, nj))

    return mate

def move():
    for t in team:
        ci, cj = t
        for di in directions:
            ni, nj = ci + di[0], cj + di[1]
            if ni < 0 or nj >= n or ni < 0 or nj >= n: continue
            if arr[ni][nj] == 4:
                arr[ni][nj] = arr[ci][cj]
                arr[ci][cj] = 4

    print(arr)

def ball(dr):
    tran_arr = list(map(list, zip(*arr)))
    if dr == 0:
        # 오른쪽
        for i in arr[ball_idx]:
            # 해당 인덱스의 처음 0이 아닌 값을 리턴
            if 0 < i < 4:
                return i
    elif dr == 1:
        # 위쪽
        for i in tran_arr[ball_idx]:
            if 0 < i < 4:
                return i
    elif dr == 2:
        # 왼쪽
        for i in reversed(arr[ball_idx]):
            if 0 < i < 4:
                return i
    else:
        # 아래쪽
        for i in reversed(tran_arr[ball_idx]):
            if 0 < i < 4:
                return i

    return -1

def find_team(i, j):
    if (i, j) in teams:
        return team_idx


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = 0
ans = 0

print(arr)

# [1] 각 팀의 머리 좌표 반환
head = head_team()
teams ={}
team_idx = 0
ball_idx = 0

for i, j in head:
    # [2] 각 팀의 구성원들 찾기
    team = bfs(i, j)
    teams[team_idx] = team
    team_idx += 1
print("teams:", teams)
for _ in range(k):
    # [3] 이동하기
    move()

    # [4] 공 던지기
    if ball_idx == n-1: # n행 혹은 n열까지 이동시 다시 ball idx 초기화하고 방향 전환
        ball_idx = 0
        dr = (dr + 1) % 4

    target = ball(dr) ** 2
    if target != -1:
        ans += target

print(ans)