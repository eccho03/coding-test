import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    
    if my_map[x][y] != 0:
        my_map[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y+1)
        dfs(x-1, y-1)
        dfs(x+1, y+1)
        dfs(x+1, y-1)
        return True
    return False


while True:
    w, h = map(int, input().split())
    if (w == 0 and h == 0):
        break
    my_map = [[0] * w for _ in range(h)]

    idx = 0
    for _ in range(h):
        arr = list(map(int, input().split()))
        my_map[idx] = arr
        idx += 1

    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                cnt += 1

    print(cnt)