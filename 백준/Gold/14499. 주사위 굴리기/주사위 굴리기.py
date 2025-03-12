def move_dice(direct):
    global x, y, dice

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    nx, ny = x + dx[direct-1], y + dy[direct-1]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        return None

    x, y = nx, ny

    if direct == 1:
        # 동쪽
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direct == 2:
        # 서쪽
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direct == 3:
        # 북쪽
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:
        # 남쪽
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    return dice


n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

for com in command:
    # print("command:",com)
    new_dice = move_dice(com)
    if new_dice:
        dice = new_dice
        if graph[x][y] == 0:
            graph[x][y] = dice[5]
        else:
            dice[5] = graph[x][y]
            graph[x][y] = 0
        print(dice[0])
        # print("답: ",dice[0])
