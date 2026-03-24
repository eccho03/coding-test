from collections import deque
def bfs(si, sj, target):
    q = deque()
    v = [[0]*N for _ in range(N)]
    group = []

    q.append((si, sj))
    v[si][sj]=1
    group.append((si, sj))

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and (arr[ni][nj]==0 or arr[ni][nj]==target):
                q.append((ni, nj))
                group.append((ni, nj))
                v[ni][nj]=1

    return group

def print_arr(num, arr):
    print(f'#{num}')
    for row in arr:
        print(*row)
    print()

def make_group(num, group):
    block = [[0]*N for _ in range(N)]
    for i,j in group:
        block[i][j]=1

    # print_arr(num, block)

    return group

def check_group(group):
    # 일반 블록이 하나라도 있는지 체크
    flag = False
    for i, j in group:
        if 1<=arr[i][j]<=M:
            flag=True
            break

    if not flag: return False

    # 블록 개수 >= 2
    if len(group)<2: return False

    return True

def find_standard(group):
    group.sort()
    rainbow_cnt = 0
    for i, j in group:
        if arr[i][j]==0:
            rainbow_cnt+=1

    for i, j in group:
        if arr[i][j]!=0 and arr[i][j]!='*':
            return i, j, rainbow_cnt
    return -1, -1, rainbow_cnt

def move(arr):
    for i in range(N-2,-1,-1):
        for j in range(N):
            if arr[i][j]==-1 or arr[i][j]=='*': continue
            idx = i
            while True:
                if idx==N-1: break
                if arr[idx+1][j]=='*':
                    arr[idx+1][j] = arr[idx][j]
                    arr[idx][j] = '*'
                else:
                    break
                idx+=1

    # print_arr("중력작용", arr)

def rotate(arr):
    copy_arr = [x[:] for x in arr]
    # print(copy_arr)

    for i in range(N):
        for j in range(N):
            arr[N-j-1][i] = copy_arr[i][j]

    # print_arr("회전후",arr)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

while True:
    '''
    1. 크기가 가장 큰 블록 그룹 찾기
    '''
    possible_block_groups = []
    for num in range(1, M+1):
        for i in range(N):
            for j in range(N):
                if arr[i][j]==num:
                    cur_group = make_group(num, bfs(i, j, num))

                    if check_group(cur_group):
                        ti, tj, rainbow_cnt = find_standard(cur_group)
                        # 크기   /   무지개 블록 수   /   행,열  / 블록 그룹 좌표 목록
                        possible_block_groups.append((len(cur_group), rainbow_cnt, ti, tj, cur_group))

    if len(possible_block_groups)==0: break # 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복되어야 한다.

    possible_block_groups.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    target = possible_block_groups[0]

    for i, j in target[-1]:
        arr[i][j]='*'

    answer+=target[0]**2

    # print_arr('*한 이후', arr)
    # print(target[0])

    '''
    2. 중력 작용
    '''
    move(arr)

    '''
    3. 반시계 회전
    '''
    rotate(arr)

    '''
    4. 중력 작용
    '''
    move(arr)

print(answer)