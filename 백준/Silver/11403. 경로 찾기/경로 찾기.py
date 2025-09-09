INF = float('inf')
def floyd_warshall():
    dist = [[INF]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dist[i][j] = arr[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]==0:
            arr[i][j]=INF

dist = floyd_warshall()
ans = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if 0<dist[i][j]<INF:
            ans[i][j]=1
        else:
            ans[i][j]=0

for i in range(N):
    print(*ans[i])
