from collections import deque

def bfs(si,sj,ei,ej):
    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((si,sj, 0))
    v[si][sj]=1

    while q:
        ci,cj,cnt = q.popleft()
        if (ci,cj)==(ei,ej):
            return cnt

        for di,dj in ((-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)):
            ni,nj = ci+di, cj+dj

            # 네방향,범위내,미방문,조건=x
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni,nj,cnt+1))
                v[ni][nj]=1

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    si,sj = map(int, input().split())
    ei,ej = map(int, input().split())

    ans = bfs(si,sj,ei,ej)
    print(ans)