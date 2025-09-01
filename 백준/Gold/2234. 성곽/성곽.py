from collections import deque
def bfs(si,sj,room_number):
    q = deque()

    q.append((si,sj))
    v[si][sj]=1
    size=1
    room_id[si][sj] = room_number

    while q:
        ci,cj = q.popleft()
        wall = format(arr[ci][cj], '04b')
        # print(wall)
        for i in range(4):
            di, dj = directions[i]
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 \
                and wall[i]=='0':
                q.append((ni,nj))
                v[ni][nj]=1
                room_id[ni][nj] = room_number
                size+=1
    return size



M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
directions = [(1,0), (0,1), (-1,0), (0,-1)] #남동북서

room_cnt = 0
room_size = dict()
room_id = [[0]*M for _ in range(N)]
room_number = 1
for i in range(N):
    for j in range(M):
        if v[i][j]==0:
            cur_room_size = bfs(i,j,room_number)
            room_size[room_number] = cur_room_size
            room_number+=1

mx_after_remove = 0
for i in range(N):
    for j in range(M):
        wall = format(arr[i][j], '04b')
        for dir in range(4):
            di, dj = directions[dir]
            if wall[dir]=='1':
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M:
                    if room_id[i][j]!=room_id[ni][nj]:
                        combined = room_size[room_id[i][j]] + room_size[room_id[ni][nj]]
                        mx_after_remove = max(mx_after_remove, combined)

print(len(room_size))
print(max(room_size.values()))
print(mx_after_remove)