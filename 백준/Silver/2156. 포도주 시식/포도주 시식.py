N=int(input())
grape = [int(input()) for _ in range(N)]
d = [0] * N

if N==1:
    print(grape[0])
elif N==2:
    print(grape[0]+grape[1])
else:
    d[0]=grape[0]
    d[1]=grape[0]+grape[1]
    d[2]=max(grape[0]+grape[1],grape[1]+grape[2], grape[0]+grape[2])

    for i in range(3,N):
        d[i]=max(d[i-3]+grape[i-1]+grape[i],d[i-2]+grape[i], d[i-1])
    print(max(d))