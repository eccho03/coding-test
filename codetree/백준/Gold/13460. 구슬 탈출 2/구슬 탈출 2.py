def find_ri_rj():
    for i in range(N):
        for j in range(M):
            if board[i][j]=='R':
                return i, j
    return -1, -1

def find_bi_bj():
    for i in range(N):
        for j in range(M):
            if board[i][j]=='B':
                return i, j
    return -1, -1

def find_ei_ej():
    for i in range(N):
        for j in range(M):
            if board[i][j]=='O':
                return i, j
    return -1, -1

def roll(ci,cj, di,dj):
    # 빨간구슬 끝까지 떨어지기
    dist=0
    while True:
        ci, cj = ci+di, cj+dj
        dist+=1

        if board[ci][cj]=='O':
            break

        elif board[ci][cj]=='#':
            ci, cj = ci-di, cj-dj  # roll-back
            dist-=1
            break
    return ci,cj,dist

from collections import deque
def bfs(sri,srj,sbi,sbj):
    q = deque()
    v = set()

    q.append((sri,srj,sbi,sbj,0))
    v.add((sri,srj,sbi,sbj))

    while q:
        cri,crj,cbi,cbj,cnt = q.popleft()
        #print(cri,crj,cbi,cbj,cnt)
        if cnt>=10:
            break

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):

            nri,nrj,r_dis = roll(cri,crj,di,dj)
            nbi,nbj,b_dis = roll(cbi,cbj,di,dj)

            if (nri,nrj)==(ei,ej) and (nbi,nbj)!=(ei,ej):
                return cnt+1
            elif (nbi,nbj)==(ei,ej):
                continue

            if (nri,nrj)==(nbi,nbj):
                if r_dis>b_dis:
                    nri,nrj=nri-di,nrj-dj
                else:
                    nbi,nbj=nbi-di,nbj-dj

            if (nri,nrj,nbi,nbj) not in v:
                q.append((nri,nrj,nbi,nbj,cnt+1))
                v.add((nri,nrj,nbi,nbj))

    return -1


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

ri, rj = find_ri_rj()
bi, bj = find_bi_bj()
ei, ej = find_ei_ej()
#print(ri,rj,bi,bj,ei,ej)
ans = bfs(ri, rj, bi, bj)
print(ans)

