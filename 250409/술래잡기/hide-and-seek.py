import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def myarr():
    for i in range(N):
        print(*arr[i])
    print()

    print("술래좌표:",ti,tj, td)
    print("나무 좌표:",tree)
    print("도망자좌표: ",runner)

def find_runner():
    ilst=[]
    for idx in runner:
        i, j, d = runner[idx]
        if (i, j) == (ai, aj):
            ilst.append(idx)
    return ilst

di = [0, 0, 1, -1] # 좌 우 하 상
dj = [-1, 1, 0, 0]
opp={0:1, 1:0, 2:3, 3:2}

tdi = [-1, 0, 1, 0] # 술래 시계 방향
tdj = [0, 1, 0, -1] # 상 우 하 좌

N, M, H, K = map(int, input().split())
arr = [[0]*N for _ in range(N)]
runner = {}
for idx in range(M):
    i, j, d = map(int, input().split())
    arr[i-1][j-1] += 1 #0-based
    runner[idx] = [i-1,j-1,d]

tree = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(H)] #0-based

# [0] 술래의 위치 구하기
ti, tj, td = N//2, N//2, 0

cnt = 0
mx_cnt = 0
ans = 0
# K턴 반복
for T in range(1, K+1): # 턴 1부터 시작 !!
    # [1] 도망자 이동
    for idx in runner:
        ci, cj, dr = runner[idx]
        if abs(ci-ti)+abs(cj-tj)<=3: #현재 술래와 거리 <=3만 움직임
            ni, nj = ci+di[dr], cj+dj[dr]
            if ni<0 or ni>=N or nj<0 or nj>=N: # 범위 밖이라면
                dr = opp[dr]
                ni, nj = ci + di[dr], cj + dj[dr]
            if (ni, nj) == (ti, tj):    continue # 움직이려는 칸에 술래 => 안 움직임

            runner[idx] = [ni, nj, dr] # 도망자 정보 업데이트

            arr[ni][nj]=arr[ci][cj] # 맵 상에서도 도망자 위치 업데이트
            arr[ci][cj]=0

    # [2] 술래 이동
    #print("술래좌표:", ti, tj, td)

    cnt+=1

    tni, tnj = ti+tdi[td], tj+tdj[td]

    if (T//(N*N))%2 == 0:
        #시계방향 진행

        if (ti,tj)==(N//2,N//2):
            td = (td + 1) % 4  # 시계방향 회전
            cnt=0
            mx_cnt = 1

        elif cnt==mx_cnt:
            td=(td+1)%4 #시계방향 회전
            cnt=0
            mx_cnt += 1
    else:
        if (ti, tj) == (0, 0):
            td = (td - 1) % 4  # 반시계방향 회전
            cnt = 0
            mx_cnt = 1

        elif cnt == mx_cnt:
            td = (td - 1) % 4  # 반시계방향 회전
            cnt = 0
            mx_cnt += 1

    ti,tj=tni,tnj
    #print("이동후 술래좌표:",ti,tj,td)

    # [3] 술래가 도망자 잡기
    target=[]
    for i in range(0,3):
        ai,aj = ti+(tdi[td])*i, tj+(tdj[td])*i
        target.append((ai,aj))
    #print("target",target)
    for ai, aj in target:
        if 0<=ai<N and 0<=aj<N and arr[ai][aj]>=1 and (ai,aj) not in tree:
            # 범위 내 / 나무 x
            ans += T*arr[ai][aj]
            arr[ai][aj]=0
            ilst=find_runner()
            for idx in ilst:
                runner.pop(idx)

    if not runner:
        break
    #myarr()  # 디버깅용

print(ans)