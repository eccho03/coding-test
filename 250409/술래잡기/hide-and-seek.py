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
        if abs(arr[i][0] - ti) + abs(arr[i][1] - tj) <= 3:  # 술래와 거리 3이하인 경우 이동
            ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
            if 1 <= ni <= N and 1 <= nj <= N:  # 범위내면 술래체크
                if (ni, nj) != (ti, tj):  # 술래위치가 아니면 이동
                    arr[i][0], arr[i][1] = ni, nj
            else:  # 범위밖=>방향 반대
                arr[i][2] = opp[arr[i][2]]  # 반대 방향전환 및 저장
                ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
                if (ni, nj) != (ti, tj):
                    arr[i][0], arr[i][1] = ni, nj

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
