from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])
    v = set()
    v.add((si, sj))

    max_ci = 0

    while q:
        ci, cj = q.popleft()
        max_ci = max(max_ci, ci)

        for i in range(4):
            # 네 방향, 미방문, 조건 : 나 자신이거나 상대방이 골렘이고 내 출구일 때
            ni, nj = ci + di[i], cj + dj[i]

            if (ni, nj) not in v and (arr[ci][cj] == arr[ni][nj] or (arr[ni][nj] > 1 and (ci, cj) in exit_set)):
                v.add((ni, nj))
                q.append((ni, nj))

    return max_ci-2

R, C, K = map(int, input().split())
golam_loc = []
unit = [list(map(int, input().split())) for _ in range(K)]
arr = [[1] + [0] * C +[1] for _ in range(R + 3)] + [[1] * (C + 2)]  # 전체 맵 - R + 3 * C / 벽은 1로 둘러싸기
exit_set = set() # 출구 정보

di = [-1, 0, 1, 0]  # 상 우 하 좌
dj = [0, 1, 0, -1]

num = 2
ans = 0

for cj, dr in unit: # 중앙 좌표 / 방향
    ci = 1 # 시작 좌표 1

    # [1] 골렘 : 이동 가능한 남쪽까지 이동
    while True:
        # 이동 가능할 때까지 이동
        if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0:
            # 남쪽 이동
            ci += 1
        elif (arr[ci-1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-1]) + (arr[ci+1][cj-2] + arr[ci+2][cj-1]) == 0:
            # 서쪽 이동
            cj -= 1
            ci += 1
            dr = (dr - 1) % 4 # 반시계 방향으로 전환
        elif (arr[ci-1][cj+1] + arr[ci][cj+2] + arr[ci+1][cj+1]) + (arr[ci+2][cj+1] + arr[ci+1][cj+2])== 0:
            # 동쪽 이동
            cj += 1
            ci += 1
            dr = (dr + 1) % 4 # 시계 방향으로 전환
        else:
            break

    # [2] 골렘 표시
    if ci < 4:
        # 골렘이 천장 밖으로 나옴
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)] # 배열 초기화
        num = 2
        exit_set = set() # 출구 정보 초기화
    else :
        # 골렘을 배열에 표시
        arr[ci-1][cj], arr[ci+1][cj], arr[ci][cj-1], arr[ci][cj+1],arr[ci][cj] = [num]*5
        num += 1
        exit_set.add((ci + di[dr], cj + dj[dr])) # 비상구 위치 추가

        ans += bfs(ci, cj)

print(ans)