N = int(input())

if N==0:
    print(0)
else:
    d = [0]*(N+1)
    d[0], d[1] = 0, 1
    for i in range(2,N+1):
        d[i]=d[i-1]+d[i-2]

    print(d[N])