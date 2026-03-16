# 상하좌우 이동
# 승객을 도착지에 내려주면 연료충전, 연료 바닥나면 업무종료
# M명 태우는게 목표
# 최단경로 이동

# 1. 백준의 현재위치에서 최단거리인 승객고르기
# 2. 승객까지 이동 (택시=승객위치 ㄱㄴ, 한칸 이동시 연료 -1)
# 3. 한 승객 태우면 연료*2

from collections import deque
def bfs(si,sj):
    q = deque()
    dist = [[-1]*N for _ in range(N)]

    q.append((si,sj))
    dist[si][sj]=0

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj

            if 0<=ni<N and 0<=nj<N and dist[ni][nj]==-1 and arr[ni][nj]==0:
                q.append((ni,nj))
                dist[ni][nj]=dist[ci][cj]+1

    return dist

N, M, amount = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
driver_i, driver_j = map(lambda x: int(x)-1, input().split()) # 1based ->0based
customers = []
for _ in range(M):
    cust_si,cust_sj,cust_ei,cust_ej = map(lambda x: int(x)-1,input().split())
    customers.append((cust_si,cust_sj,cust_ei,cust_ej))
#--------------------
customers.sort(key=lambda x: (x[0], x[1])) # 거리 같은 경우에는 행/열 가까운 순으로

for i in range(M):
    mn_dist=N*M+1
    driver_dist = bfs(driver_i, driver_j)
    for j in range(M-i):
        cust_si, cust_sj, cust_ei, cust_ej = customers[j]
        mn_dist = min(mn_dist, driver_dist[cust_si][cust_sj])

    if mn_dist==-1:
        print("-1")
        exit(0)

    target_idx=-1
    for j in range(M-i):
        cust_si, cust_sj, cust_ei, cust_ej = customers[j]
        if driver_dist[cust_si][cust_sj]==mn_dist:
            target_idx=j
            break

    cust_si, cust_sj, cust_ei, cust_ej = customers[target_idx]
    amount -= mn_dist # 택시 초기 위치 ~ 승객
    if amount<0:
        print("-1")
        exit(0)

    drive_dist = bfs(cust_si, cust_sj)
    amount -= drive_dist[cust_ei][cust_ej]
    if amount<0:
        print("-1")
        exit(0)

    amount += drive_dist[cust_ei][cust_ej]*2 # 승객 승차 ~ 하차
    driver_i, driver_j = cust_ei, cust_ej # 택시 위치 이동
    customers.pop(target_idx) # 해당손님 제거

    # print(amount, driver_i, driver_j)
    # print(customers)

print(amount)

