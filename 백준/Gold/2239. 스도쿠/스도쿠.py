N=9
arr = [list(map(int, list(input().strip()))) for _ in range(N)]
blanks = [(i, j) for i in range(9) for j in range(9) if arr[i][j]==0]

def is_valid(x, y, num):
    for idx in range(N):
        if arr[x][idx]==num or arr[idx][y]==num:
            return False

    si, sj = (x//3)*3, (y//3)*3
    for i in range(N//3):
        for j in range(N//3):
            if arr[si+i][sj+j]==num:
                return False

    return True

def dfs(idx):
    if idx == len(blanks):
        for row in arr:
            print(''.join(map(str, row)))
        exit(0)

    x, y = blanks[idx]

    for num in range(1, 10):
        if is_valid(x, y, num):
            arr[x][y] = num
            dfs(idx+1)
            arr[x][y] = 0

dfs(0)