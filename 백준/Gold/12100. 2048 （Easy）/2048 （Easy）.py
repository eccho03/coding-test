import copy

def find_block(arr):
    max_block = 0
    for i in range(n):
        for j in range(n):
            max_block = max(max_block, arr[i][j])

    return max_block

def left(board):
    new_board = copy.deepcopy(board)
    # 왼쪽
    for i in range(n):
        check = 0
        for j in range(1, n):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[i][check] == 0:
                    new_board[i][check] = tmp

                elif new_board[i][check] == tmp:
                    new_board[i][check] = tmp*2
                    check += 1
                else:
                    check += 1
                    new_board[i][check] = tmp
    return new_board

def right(board):
    new_board = copy.deepcopy(board)
    # 오른쪽
    for i in range(n):
        check = n - 1
        for j in range(n-1, -1, -1):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[i][check] == 0:
                    new_board[i][check] = tmp

                elif new_board[i][check] == tmp:
                    new_board[i][check] = tmp*2
                    check -= 1
                else:
                    check -= 1
                    new_board[i][check] = tmp
    # print(new_board)
    return new_board

def up(board):
    new_board = copy.deepcopy(board)
    # 윗쪽
    for j in range(n):
        check = 0
        for i in range(n):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[check][j] == 0:
                    new_board[check][j] = tmp

                elif new_board[check][j] == tmp:
                    new_board[check][j] = tmp*2
                    check += 1
                else:
                    check += 1
                    new_board[check][j] = tmp
    # print(new_board)
    return new_board

def down(board):
    new_board = copy.deepcopy(board)

    # 아랫쪽
    for j in range(n):
        check = n-1
        for i in range(n-1, -1, -1):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[check][j] == 0:
                    new_board[check][j] = tmp

                elif new_board[check][j] == tmp:
                    new_board[check][j] = tmp*2
                    check -= 1
                else:
                    check -= 1
                    new_board[check][j] = tmp
    # print(new_board)
    return new_board

def dfs(cnt, board):
    global ans
    if cnt == 5:
        ans = max(ans, find_block(board))
        return ans  # 최댓값 반환

    return max(
        dfs(cnt + 1, left(board)),
        dfs(cnt + 1, right(board)),
        dfs(cnt + 1, up(board)),
        dfs(cnt + 1, down(board))
    )

n = int(input())
ans = 0
board = [list(map(int, input().split())) for _ in range(n)]

answer = dfs(0, board)
print(answer)