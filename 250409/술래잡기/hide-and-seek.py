import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def myarr():
    for i in range(N):
        print(*arr[i])
    print()

    print("술래좌표:", ti, tj, td)
    print("나무 좌표:", tree)

N, M, H, K = map(int, input().split())

# 도망자 좌표 입력
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))

# 나무좌표 입력
tree = set()
for _ in range(H):
    i,j=map(int, input().split())
    tree.add((i,j))

# 0(좌) 1(우) 2(하) 3(상)
di = [ 0, 0, 1,-1]
dj = [-1, 1, 0, 0]
opp = {0:1, 1:0, 2:3, 3:2}  # 반대방향

# 방향  상 우 하 좌   tagger(술래)방향 (바깥으로 돌 때 방향)
tdi = [-1, 0, 1, 0]
tdj = [ 0, 1, 0,-1]

mx_cnt, cnt, flag, val = 1, 0, 0, 1
ti,tj,td = (N+1)//2, (N+1)//2, 0

ans = 0

# K턴 반복
for T in range(1, K + 1):  # 턴 1부터 시작 !!
    # [1] 도망자 이동
    for i in range(len(arr)):
        ci, cj, dr = arr[i]
        if abs(ci - ti) + abs(cj - tj) <= 3:  # 현재 술래와 거리 <= 3만 움직임
            ni, nj = ci + di[dr], cj + dj[dr]
            if (ni, nj) == (ti, tj):  continue  # 움직이려는 칸에 술래 => 안 움직임
            if not (1<=ni<=N and 1<=nj<=N):  # 범위 밖이라면
                dr = opp[dr]
                ni, nj = ci + di[dr], cj + dj[dr]
                if (ni, nj) == (ti, tj):  continue
            ci,cj=ni,nj
            arr[i]=[ni,nj,dr]

    # [2] 술래의 이동
    cnt += 1
    ti, tj = ti + tdi[td], tj + tdj[td]
    if (ti, tj) == (1, 1):  # 안쪽으로 동작하는 달팽이
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2  # 초기방향은 아래로(하)
    elif (ti, tj) == ((N+1)//2, (N+1)//2):  # 바깥으로 동작하는 달팽이
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if cnt == mx_cnt:  # 방향 변경
            cnt = 0
            td = (td + val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0  # 두 번에 한 번씩 길이 증가
                mx_cnt += val

    # [3] 술래가 도망자 잡기
    target = []
    # 술래가 잡을 수 있는 위치 계산
    for i in range(3):  # 술래의 타겟 위치를 계산
        ai, aj = ti + (tdi[td]) * i, tj + (tdj[td]) * i
        target.append((ai, aj))

    for i in range(len(arr) - 1, -1, -1):
        ci, cj, dr = arr[i]
        if (ci, cj) in target and (ci, cj) not in tree:
            arr.pop(i)
            ans += T
    # 도망자가 없다면 더이상 점수도 없음
    if not arr:
        break
# myarr()  # 디버깅용

print(ans)
