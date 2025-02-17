def move(location, direction):
    new = location[-1][:]
    new[0] += directions[direction][0]  # X 좌표
    new[1] += directions[direction][1]  # Y 좌표
    return new

def check_game(location):
    head = location[-1]
    if head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n:
        return True
    
    if head in location[:-1]:
        return True

    return False
    
def check_apple(location):
    if location[-1] in apple_loc:
        apple_loc.remove(location[-1])
        return True
    return False

n = int(input())
k = int(input())

apple_loc = []
for _ in range(k):
    row, col = map(int, input().split())
    apple_loc.append([row - 1, col - 1])

snake_move = []
l = int(input())
for _ in range(l):
    x, c = map(str, input().split())
    snake_move.append([int(x), c])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상
cur_direct = 0

time = 0
snake_location = [[0, 0]]

while True:
    time += 1

    new = move(snake_location, cur_direct)
    snake_location.append(new)

    if check_game(snake_location):
        break

    if not check_apple(snake_location):
        snake_location.pop(0)

    if snake_move and snake_move[0][0] == time:
        _, turn  = snake_move.pop(0)
        if turn == 'D':
            cur_direct = (cur_direct + 1) % 4
        else:
            cur_direct = (cur_direct - 1) % 4
print(time)