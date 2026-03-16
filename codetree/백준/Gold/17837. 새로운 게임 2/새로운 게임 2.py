# N*N, 말 1~K번
# 각 칸: 흰빨파
# 상하좌우
# 위에 올려진 말들도 같이 이동
# 종료조건 - 한 칸에 말이 4개 이상
import math

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]
player = [list(map(int, input().split())) for _ in range(K)] # 1-based
# print(player)

directions = [(0,0), (0,1), (0,-1), (-1,0), (1,0)] # 우좌상하

for idx, (r, c, _) in enumerate(player):
    arr[r-1][c-1].append(idx+1)

# print(arr)


def find_player(num):
    for i in range(N):
        for j in range(N):
            if num in arr[i][j]:
                return i, j
    return -1,-1

TURN = 1
num = 0 # player 번호
change_dir = {1:2, 2:1, 3:4, 4:3}

while True:
    if TURN>1000: # 턴이 1000보다 큰데 종료 안 된 경우
        TURN=-1
        break

    # print("현재 플레이어: " + str(num + 1) + "번")
    ci, cj = find_player(num + 1)
    # print(ci, cj)
    dir = player[num][2]
    di, dj = directions[dir]

    ni, nj = ci+di, cj+dj

    if not (0<=ni<N and 0<=nj<N) or board[ni][nj]==2:  # 이동하려는 칸이 파란색 / 범위밖
        rev_dir = change_dir[dir]  # 반대방향
        di, dj = directions[rev_dir]
        ni, nj = ci+di, cj+dj
        player[num][2] = rev_dir

        if not (0<=ni<N and 0<=nj<N) or board[ni][nj]==2:
            num += 1
            if num >= K:
                num = 0
                TURN += 1
            continue

        target = arr[ci][cj]
        idx = target.index(num + 1)
        move, left = target[idx:], target[:idx]
        arr[ci][cj] = left

        if board[ni][nj] == 0:  # 이동하려는 칸이 흰색
            arr[ni][nj].extend(move)
        else:
            arr[ni][nj].extend(move[::-1])

    elif board[ni][nj] == 0:  # 이동하려는 칸이 흰색
        target = arr[ci][cj]
        idx = target.index(num + 1)
        move, left = target[idx:], target[:idx]
        arr[ci][cj] = left

        arr[ni][nj].extend(move)

    else:  # 이동하려는 칸이 빨간색
        target = arr[ci][cj]
        idx = target.index(num + 1)
        move, left = target[idx:], target[:idx]
        arr[ci][cj] = left

        arr[ni][nj].extend(move[::-1])

    if len(arr[ni][nj]) >= 4:
        break

    num+=1
    if num>=K:
        num=0
        TURN+=1
    #     print(TURN)
    #
    # print(arr)
    # print(player)

print(TURN)