import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def find_base():
    base = set()
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] == 1:
                base.add((i,j))
                arr[i][j] = 0 # 0으로 만들어서 지도로 쓰자!
    return base

N, M = map(int, input().split())
arr = [[1]*(N+2)]+[[1]+list(map(int, input().split()))+[1] for _ in range(N)]+[[1]*(N+2)] # 전체 좌표
store = dict()
for m in range(1,M+1):
    r,c = map(int, input().split())
    store[m] = (r,c)

basecamp = find_base() # base 위치를 좌표로 제공

from collections import deque
def find(si, sj, dest): # 시작좌표에서 목적지 좌표들(set) 중 최단거리 동일반경 리스트를 모두 찾기!
    q = deque()
    v = [[0]*(N+2) for _ in range(N+2)]
    tlst=[]

    q.append((si, sj))
    v[si][sj]=1

    while q:
        nq = deque() # 동일 (범위)반경까지 처리
        for ci, cj in q:
            if (ci,cj) in dest: # 목적지 찾음! => 더 뻗어나갈 필요 없음
                tlst.append((ci,cj))
            else: # 범위내(막았으니 필요x), 네방향, 미방문, 조건 => arr[ni][nj]==0
                for di, dj in ((-1,0),(0,-1),(0,1),(1,0)): # 어차피 여러 개면 밑에서 우선순위 고려하니까 순서는 상관없음
                    ni, nj = ci+di, cj+dj
                    if v[ni][nj]==0 and arr[ni][nj]==0:
                        nq.append((ni,nj))
                        v[ni][nj]=v[ci][cj]+1
        if len(tlst)>=1:
            tlst.sort(key=lambda x:(x[0],x[1])) #여러 개일 수도 있으므로
            return tlst[0]
        q = nq
    return -1 # 도달 안 하기는 함

def solve():
    q = deque()
    T = 1
    arrived = [0] * (M+1) # 0이면 미도착, >0이면 도착시간
    alst = []

    while q or T==1: # 이동할 사람이 있는 동안
        nq = deque()
        # [1] 모두 편의점방향 최단거리 이동 (이번 time만, 같은 반경)
        for ci, cj, num in q:
            if arrived[num]==0: # 도착하지 않은 사람만 처리
                # 편의점 방향 최단거리(우선순위) 한 칸 이동
                ni, nj = find(store[num][0], store[num][1], set(((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj))))

                if (ni,nj)==(store[num][0], store[num][1]):
                    arrived[num] = T
                    alst.append((ni,nj)) # 통행 금지는 모두 이동 후 처리해야 함!!
                else:
                    nq.append((ni,nj,num))
        q=nq
        # [2] 편의점 도착 처리
        if len(alst)>=1:
            for i,j in alst:
                arr[i][j]=1

        # [3] 시간번호의 멤버가 베이스캠프로 이동

        if T <= M:
            si, sj = store[T]
            ei, ej = find(si, sj, basecamp) # 가장 가까운, 우선순위 베이스 캠프 골라서 이동
            basecamp.remove((ei, ej))
            arr[ei][ej]=1
            q.append((ei, ej, T))
        T += 1
    return max(arrived)


ans = solve()
print(ans)