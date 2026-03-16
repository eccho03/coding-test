def print_arr(arr):
    for i in range(N):
        print(*arr[i])
    print()

def make_cloud(loc):
    cloud = [[0]*N for _ in range(N)]
    for i, j in loc:
        cloud[i][j]=1

    return cloud

def move_cloud(cloud, dir, dist):
    cloud_loc = [(i, j) for i in range(N) for j in range(N) if cloud[i][j]==1]
    new_loc = []
    directions = [(0, 0),(0,-1),(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1)]

    for i,j in cloud_loc:
        di, dj = directions[dir]
        ni, nj = (i+di*dist)%N, (j+dj*dist)%N
        new_loc.append((ni, nj))

    cloud = make_cloud(new_loc)

    return cloud, new_loc

def make_new_cloud(cloud_loc):
    new_cloud_loc = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in cloud_loc and arr[i][j]>=2:
                arr[i][j]-=2 # 구름이 생겨서 물의 양이 2만큼 줄어듦
                new_cloud_loc.append((i, j))

    cloud = make_cloud(new_cloud_loc)
    return cloud, new_cloud_loc

def rain_cloud(arr):
    for i in range(N):
        for j in range(N):
            if cloud[i][j]==1:
                arr[i][j]+=1
    return arr

def check_cloud(cloud_loc):
    for i, j in cloud_loc:
        cnt = 0
        target = [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]

        for ni, nj in target:
            # print(f'구름 위치: ({i},{j}), 대각선 체크: ({ni}, {nj})')
            #  이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아님
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] > 0:
                    cnt += 1
        arr[i][j] += cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

# print(arr)
# print(move)

cloud = [[0]*N for _ in range(N)]

# 초기 구름 위치
cloud[N-1][1-1]=1
cloud[N-1][2-1]=1
cloud[N-1-1][1-1]=1
cloud[N-1-1][2-1]=1

# print_arr(cloud)

# 모든 구름이 di 방향으로 si칸 이동

for di, si in move:
    cloud, cloud_loc = move_cloud(cloud, di, si)
    # print_arr(cloud)

    # 각 구름에서 비가 내려 구름 칸 바구니 물 양 1 증가
    arr = rain_cloud(arr)
    # print_arr(arr)

    cloud = [[0]*N for _ in range(N)] # 구름 사라짐

    # 물복사버그 마법 시전
    check_cloud(cloud_loc)
    # print_arr(arr)

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어듦
    cloud, cloud_loc = make_new_cloud(cloud_loc)

    # print_arr(cloud)
    # print_arr(arr)

ans = sum(map(sum, arr))
print(ans)