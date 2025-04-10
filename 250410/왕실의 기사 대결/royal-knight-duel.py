import sys
sys.stdin = open('input.txt','r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌

from collections import deque
def push_unit(start, dr):
    q = deque()
    pset = set()
    damage = [0]*(M+1)

    q.append(start)
    pset.add(start)

    while q:
        cur = q.popleft()
        ci,cj,h,w,k = knight[cur]

        # 명령받은 방향진행, 벽이아니면, 겹치는 다른조각이면 => 큐에 삽입
        ni,nj = ci+di[dr], cj+dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j]==2:    return
                if arr[i][j]==1 and cur!=start:
                    damage[cur]+=1

        # 벽은 아니 / 모두 다 이동했을 때 데미지 처리를 해야 함 !! 그전에 삭제돼버리면 안 밀릴 수도 있기 때문에
        # 겹치는 다른 유닛 있는 경우 모두 큐에 추가
        for idx in knight:
            if idx in pset: continue    # 이미 움직일 대상이면 체크할 필요없음

            ti,tj,th,tw,tk=knight[idx]
            # 겹치는 경우
            if ni<=ti+th-1 and ni+h-1>=ti and tj<=nj+w-1 and nj<=tj+tw-1:
                q.append(idx)
                pset.add(idx)

    # 이동 중
    for idx in pset:
        si,sj,h,w,k = knight[idx]

        if k<=damage[idx]:
            knight.pop(idx)
        else:
            ni,nj=si+di[dr], sj+dj[dr]
            knight[idx]=[ni,nj,h,w,k-damage[idx]]


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

order = [tuple(map(int, input().split())) for _ in range(Q)]

for i, dr in order: # Q번에 걸친 왕의 명령
    if i not in knight: # 기사 목록에 없으면 아무런 반응x
        continue

    push_unit(i, dr)

# 정답 처리
ans = 0
for idx in knight:
    ans += init_k[idx]-knight[idx][4]
print(ans)