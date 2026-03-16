N,K=map(int,input().split())
d=[[0]*N for _ in range(N)]

if K==1 or N==K:
    print(1)
else:
    d[0][0] = 1
    d[1][0], d[1][1] = 1, 1

    for i in range(2,N):
        for j in range(N):
            if j==0 or j==i:
                d[i][j]=1
            else:
                d[i][j]=d[i-1][j-1]+d[i-1][j]
    print(d[N-1][K-1])