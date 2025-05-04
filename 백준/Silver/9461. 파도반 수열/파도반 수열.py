T = int(input())
for _ in range(T):
    N=int(input())
    d = [0] * N

    if 1<=N<=3:
        print(1)
    elif N==4 or N==5:
        print(2)
    else:
        d[0],d[1],d[2],d[3], d[4] = 1,1,1,2,2
        for i in range(5,N):
            d[i] = d[i-1] + d[i-5]
        print(d[N-1])