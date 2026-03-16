N=int(input())

d = [0] * (N)

if N==1:
    print(1)
elif N==2:
    print(3)
else:
    d[0]=1
    d[1]=3
    for i in range(2,N):
        d[i] = d[i-1]+2*d[i-2]
    print(d[N-1]%10007)