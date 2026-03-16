import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

K, M = map(int, input().split()) # K: 탐사 반복 횟수, M: 벽면에 적힌 유물 조각 개수
N = 5
ROT_NUM = 3

arr = [list(map(int, input().split())) for _ in range(N)]
num = list(map(int, input().split()))
ans = [] # 각 턴마다 획득한 유물 가치의 총합

def rotate(si, sj, arr):
    narr = [x[:] for x in arr]
    for i in range(ROT_NUM):
        for j in range(ROT_NUM):
            narr[si+i][sj+j] = arr[si+ROT_NUM-1-j][sj+i]
    return narr

def count_clear(arr, is_clear):
    v = [[0] * N for _ in range(N)]
    total_cnt = 0

    for i in range(N):
        for j in range(N):
            total_cnt += bfs(i, j, v, arr, is_clear)

    return total_cnt

from collections import deque
def bfs(si,sj,v,arr,is_clear):
    q = deque()
    target = set()
    cnt=0

    q.append((si, sj))
    target.add((si, sj))
    v[si][sj] = 1
    cnt+=1

    while q:
        ci, cj = q.popleft()

        # 범위내, 미방문, 조건 - arr[ci][cj]==arr[ni][nj]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                q.append((ni, nj))
                target.add((ni, nj))
                v[ni][nj] = 1
                cnt += 1

    if cnt >= 3:
        if is_clear == 1:
            for i, j in target:
                arr[i][j] = 0
        return cnt
    else:
        return 0

def myarr(arr):
    for i in range(N):
        print(*arr[i])
    print()
for _ in range(K):
    # [1] 탐사 진행
    mx_cnt = 0
    for rot in range(1, 4): # 1 ~ 4 (90, 180, 270)
        for col in range(N-ROT_NUM+1):
            for row in range(N-ROT_NUM+1):
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(row, col, narr)
                # 유물 개수 카운트
                t = count_clear(narr, 0)
                if t > mx_cnt:
                    mx_cnt = t
                    marr = narr

    if mx_cnt == 0:
        break

    # [2] 유물 획득 - 연쇄 획득 가능 !!
    total_cnt = 0
    arr = marr
    while True:
        cnt = count_clear(arr, 1)
        if cnt == 0:
            break
        total_cnt+=cnt
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = num.pop(0)

    ans.append(total_cnt)
print(*ans)