import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

R,C,K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]
arr = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]

di=[-1, 0, 1, 0]
dj=[0, 1, 0, -1] # 북 동 남 서

from collections import deque
def bfs(si, sj):
    q = deque()
    v = [[0]*(C+2) for _ in range(R+3)]

    q.append((si,sj))
    v[si][sj]=1

    mx_row=0

    while q:
        ci,cj = q.popleft()
        if ci > mx_row:
            mx_row=ci

        # 범위내, 네방향, 미방문, 조건=> arr[ni][nj]>=2일때
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if ni<0 or ni>=R+3 or nj<0 or nj>=C+2:  continue
            # 1) 골렘 자신이거나 2) 현재 골렘 출구가 다른 골렘과 인접하다면
            if v[ni][nj]==0 and arr[ni][nj]==arr[ci][cj] or ((ci,cj) in exit_set and arr[ni][nj]>=2):
                q.append((ni,nj))
                v[ni][nj]=1

    return mx_row-2


ans=0
num=2
exit_set = set()

for cj, dr in lst:
    ci = 1 # 행은 무조건 1부터 시작

    # [1] 골렘 남쪽으로 이동
    while True:
        # 남쪽으로 이동
        if arr[ci+1][cj-1]==0 and arr[ci+1][cj+1]==0 and arr[ci+2][cj]==0:
            ci+=1

        # 서쪽=>남쪽
        elif arr[ci-1][cj-1]==0 and arr[ci][cj-2]==0 and arr[ci+1][cj-1]==0 and \
                arr[ci+1][cj-2]==0 and arr[ci+2][cj-1]==0:
                ci+=1
                cj-=1
                dr = (dr-1)%4 # 반시계방향
        # 동쪽=>남쪽
        elif arr[ci-1][cj+1]==0 and arr[ci][cj+2]==0 and arr[ci+1][cj+1]==0 and \
                arr[ci+1][cj+2]==0 and arr[ci+2][cj+1]==0:
                ci+=1
                cj+=1
                dr = (dr+1)%4 # 시계방향
        else:
            break

    if ci<4:
        # 게임 재시작
        arr = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]
        exit_set.clear()
        num=2
    else:
        arr[ci-1][cj]=num
        arr[ci+1][cj]=num
        arr[ci][(cj-1):(cj+2)]=[num]*3
        num+=1
        ei, ej = ci+di[dr], cj+dj[dr]
        exit_set.add((ei,ej))
        ans+=bfs(ci,cj)
print(ans)