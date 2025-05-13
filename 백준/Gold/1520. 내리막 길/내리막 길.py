import sys
sys.setrecursionlimit(10**9)
def dfs(si, sj):
    #print(arr[si][sj], end=' ')
    if (si,sj)==(N-1,M-1):
        #print()
        return 1
    if dp[si][sj]==-1:
        dp[si][sj]=0
        for di,dj in directions:
            ni,nj = si+di, sj+dj

            if 0 <= ni < N and 0 <= nj < M and arr[si][sj] > arr[ni][nj]:
                dp[si][sj] += dfs(ni,nj)
    return dp[si][sj]


N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp =[[-1]*M for _ in range(N)]
directions = [(-1,0),(1,0),(0,-1),(0,1)]
ans = dfs(0,0)
print(ans)