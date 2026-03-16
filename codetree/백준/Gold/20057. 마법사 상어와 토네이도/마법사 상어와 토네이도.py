def print_arr(arr, N):
    for i in range(N):
        print(*arr[i])
    print()

def rotate_90(arr):
    n = len(arr)
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[i][j] = arr[j][n-i-1]
    return rotated

def make_sand_map(dir):
    sands = [[0, 0, 0.02, 0, 0],[0, 0.10, 0.07, 0.01, 0],[0.05, 0, 0, 0, 0],[0, 0.10, 0.07, 0.01, 0],[0, 0, 0.02, 0, 0]]
    c_sands = [x[:] for x in sands]

    for _ in range(dir):
        c_sands = rotate_90(c_sands)

    # print_arr(c_sands, 5)
    return c_sands

def operate_sand(ci, cj, dir):
    global answer
    total_sand = arr[ci][cj]
    cur_sands = make_sand_map(dir)
    arr[ci][cj]=0

    total_mv_sand = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            mv_sand = int(total_sand*cur_sands[i+2][j+2])
            if mv_sand <=0:     continue
            if 0<=ci+i<N and 0<=cj+j<N:
                arr[ci+i][cj+j] += mv_sand
            else:
                answer += mv_sand

            total_mv_sand += mv_sand

    remained_sand = total_sand-total_mv_sand
    if dir==0:
        if 0<=ci<N and 0<=cj-1<N:
            arr[ci][cj-1]+=remained_sand
        else:
            answer+=remained_sand
    elif dir==1:
        if 0<=ci+1<N and 0<=cj<N:
            arr[ci+1][cj]+=remained_sand
        else:
            answer+=remained_sand
    elif dir==2:
        if 0<=ci<N and 0<=cj+1<N:
            arr[ci][cj+1]+=remained_sand
        else:
            answer+=remained_sand
    else:
        if 0<=ci-1<N and 0<=cj<N:
            arr[ci-1][cj]+=remained_sand
        else:
            answer+=remained_sand


def move_tornado():
    # 좌 하 우 상
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    dir = 0
    ci, cj = N//2, N//2
    length = 1
    idx = 1
    cnt = 0
    flag = 0
    while idx != N*N:
        di, dj = directions[dir]
        ci, cj = ci+di, cj+dj

        operate_sand(ci, cj, dir)

        # print(ci, cj)
        # print_arr(v)

        cnt += 1
        idx += 1

        if cnt==length:
            dir=(dir+1)%4
            cnt=0

            if flag:
                length+=1
                flag=0
            else:
                flag=1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer=0
move_tornado()
print(answer)