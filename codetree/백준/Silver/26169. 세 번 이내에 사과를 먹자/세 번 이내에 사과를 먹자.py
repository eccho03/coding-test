import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

flag=0
def dfs(si, sj, move_cnt, apple_cnt):
    global flag
    if flag:
        return
    # ((범위내,미방문,조건=장애물x)) 아닐경우
    if si<0 or si>=N or sj<0 or sj>=N or v[si][sj]==1 or board[si][sj]==-1:
        return

    origin=board[si][sj]
    v[si][sj]=1
    if board[si][sj]==1:
        apple_cnt += 1
    board[si][sj]=-1
    #print(f'({si}, {sj}), 이동횟수: {move_cnt} 사과개수: {apple_cnt}')
    if move_cnt<=3 and apple_cnt>=2:
        flag=1
        return

    if move_cnt>3:
        v[si][sj]=0
        board[si][sj]=origin
        return

    dfs(si-1, sj, move_cnt+1, apple_cnt)
    dfs(si+1, sj, move_cnt+1, apple_cnt)
    dfs(si, sj+1, move_cnt+1, apple_cnt)
    dfs(si, sj-1, move_cnt+1, apple_cnt)

    v[si][sj]=0
    board[si][sj]=origin

N=5
board = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
v = [[0]*N for _ in range(N)]

# print(board)
dfs(r, c, 0, 0)
print(flag)