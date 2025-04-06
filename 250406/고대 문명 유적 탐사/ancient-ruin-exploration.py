import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def rotate(arr, si, sj): # 90도 시계방향 회전
    narr = [x[:] for x in arr] # 회전 대상을 narr에 복사
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+3-j-1][sj+i]
    return narr

def bfs(arr, v, si, sj, is_clear):
    q = []
    sset = set()
    cnt = 0

    q.append((si, sj))
    sset.add((si, sj))
    v[si][sj] = 1
    cnt += 1

    while q:
        ci, cj = q.pop(0)

        for di,dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            # 네방향, 범위내, 미방문, 조건: 같은 값이면
            if 0<=ni<5 and 0<=nj<5:
                if v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                    q.append((ni, nj))
                    sset.add((ni, nj))
                    v[ni][nj] = 1
                    cnt += 1

    if cnt >= 3: # 유물이면: cnt 리턴 + is_clear == 1이면 0으로 초기화
        if is_clear:
            for (i, j) in sset:
                arr[i][j] = 0
        return cnt
    else: # 유물이 아니면: 0을 리턴
        return 0

def count_clear(arr, is_clear): # clear==1인 경우 3개 이상인 값을 return
    v = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5): # 미방문인 경우 같은 값이면 fill
            if v[i][j] == 0:
                # 같은 값이면, 3개 이상인 경우
                cnt += bfs(arr, v, i, j, is_clear)
    return cnt

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
ans = []

for _ in range(K): #K번의 탐사 진행 (유물이 없는 경우 즉시 종료)
    # [1] 탐사 진행
    mx_cnt = 0
    for rot in range(1, 4): # 회전수 -> 열 -> 행 작은 순
        for sj in range(3):
            for si in range(3):
                # rot 횟수만큼 90도 시계방향 회전 => narr
                narr = [x[:] for x in arr] # 회전 전에는 항상 배열 카피
                for _ in range(rot): # rot 횟수만큼
                    narr = rotate(narr, si, sj)

                # 유물 개수 카운트
                tmp = count_clear(narr, 0) # false (clear x)
                if tmp > mx_cnt:
                    mx_cnt = tmp
                    marr = narr

    # 유물이 없는 경우 바로 탐사 종료
    if mx_cnt == 0: break

    # [2] 연쇄 획득
    cnt = 0 # 유물 개수
    arr = marr
    while True:
        tmp = count_clear(arr, 1) # true (clear o)
        if tmp == 0: break # 연쇄 획득 종료 => 다음 턴으로
        cnt += tmp # 획득한 유물 개수 누적

        # arr의 0 값인 부분 리스트에서 순서대로 추가
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)
    ans.append(cnt) # 이번 턴 연쇄 획득한 개수 추가

print(*ans)

"""
1. 유물이 아닐 때는 arr[i][j] = 0을 하면 안 되는데 q 순회 중에 하려는 논리적 오류
2. is_clear 변수를 넘겨준다.
3. rotate 할 때에는 항상 배열을 복사한다.
4. 90도 회전 - 단골이니까 확실히 숙지할 것
5. 우선순위가 있을 때 - 그 우선순위대로 for문을 돈다. 
(예) 회전 각도, 열, 행 작은 순 => for문 회전 각도, 열, 행 작은 순으로 돌기
"""
