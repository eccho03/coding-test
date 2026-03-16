def find_board(cur):
    nboard = [x[:] for x in board]
    for i in range(5):
        for j in range(5):
            if board[i][j]==cur:
                nboard[i][j] = 'X'
    return nboard

def myboard(arr):
    for i in range(5):
        print(*arr[i])
    print()

def check_board(arr):
    cnt = 0
    # 가로 체크
    for i in range(5):
        flag = False
        if arr[i][0:5]==['X', 'X', 'X', 'X', 'X']:
            flag = True
        if flag:
            cnt += 1

    #print(cnt)

    # 세로 체크
    tmp = 0
    for i in range(5):
        if arr[i][0]=='X':
            tmp += 1
    if tmp==5:
        cnt+=1

    tmp = 0
    for i in range(5):
        if arr[i][1]=='X':
            tmp += 1
    if tmp==5:
        cnt+=1

    tmp = 0
    for i in range(5):
        if arr[i][2]=='X':
            tmp += 1
    if tmp==5:
        cnt+=1

    tmp = 0
    for i in range(5):
        if arr[i][3]=='X':
            tmp += 1
    if tmp==5:
        cnt+=1

    tmp = 0
    for i in range(5):
        if arr[i][4]=='X':
            tmp += 1
    if tmp==5:
        cnt+=1

    #print(cnt)
    # 대각선 체크
    tmp = 0
    for i in range(5):
        for j in range(5):
            if i==j and arr[i][j]=='X':
                tmp+=1
    if tmp==5:
        cnt+=1

    #print(cnt)

    tmp = 0
    for i in range(5):
        for j in range(5):
            if i==5-j-1 and arr[i][j] == 'X':
                tmp += 1
    if tmp == 5:
        cnt += 1

    #print(cnt)
    return cnt

board = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]

cur = -1
ans = 0
for i in range(5):
    for j in range(5):
        ans += 1
        cur = num[i][j]

        board = find_board(cur)
        #myboard(board)
        cnt = check_board(board)
        #print(cnt)
        if cnt>=3:
            print(ans)
            exit(0)

