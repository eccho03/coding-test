import sys
sys.stdin = open('input.txt','r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌

from collections import deque
def push_unit(num, dr):
    q = deque()
    pset = set() # 이동하는 기사번호를 저장

    q.append(num)
    pset.add(num)

    si,sj,sh,sw,sk = knight[num]

    while q:
        nidx = q.popleft()
        ci, cj, h, w, k = knight[nidx]

        # 명령받은 방향 진행 / 벽이 아니면 / 겹치는 다른 조각이면 => 큐에 삽입
        ni,nj = ci+di[dr], cj+dj[dr]

        # 이동한 지점에서 데미지 / 벽에 대한 처리
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if arr[i][j]==2: # 벽이면 => 모두 취소 (밀 수 없음)
                    return
                elif arr[i][j]==1 and (i,j)!=(si,sj):
                    damage[nidx]+=1

        # 벽은 아니 / 모두 다 이동했을 때 데미지 처리를 해야 함 !! 그전에 삭제돼버리면 안 밀릴 수도 있기 때문에
        # 겹치는 다른 유닛 있는 경우 모두 큐에 추가
        for idx in knight:
            if idx in pset: continue  # 이미 움직일 대상이면 체크할 필요 x
            ti,tj,th,tw,tk = knight[idx]
            if ni<=ti+th-1 and ni+h-1>=ti and tj<=nj+w-1 and nj<=tj+tw-1:
                q.append(idx)
                pset.add(idx)

    for idx in pset:
        ki, kj, h, w, k = knight[idx]
        # 체력보다 더 큰 데미지면 삭제 처리
        if damage[idx] >= k:
            knight.pop(idx)
        # 그렇지 않다면 이동
        else:
            ni, nj = ki+di[dr], kj+dj[dr]
            knight[idx] = [ni,nj,h,w,k - damage[idx]]

N, M, Q = map(int, input().split())
arr = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
v = [[0]*(N+2) for _ in range(N+2)]
knight = {}
damage = [0] * (M+1)
init_k = [0] * (N + 1)
for idx in range(1, M+1):
    r,c,h,w,k = map(int, input().split())
    knight[idx] = [r,c,h,w,k]
    init_k[idx]=k

    for i in range(r,r+h):
        v[i][c:c+w] = [idx]*w # 디버거 동작 확인용
order = [tuple(map(int, input().split())) for _ in range(Q)]

ans=0
for i, dr in order: # Q번에 걸친 왕의 명령
    if i not in knight: # 기사 목록에 없으면 아무런 반응x
        continue

    push_unit(i, dr)

# 정답 처리
print(sum(init_k)-sum(damage))