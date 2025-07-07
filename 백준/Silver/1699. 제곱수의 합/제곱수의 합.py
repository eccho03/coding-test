import math
N=int(input())
d=[0]*(N+1)

for i in range(1,N+1):
    d[i]=i
    for j in range(1, int(math.sqrt(i)+1)):
        d[i]=min(d[i], d[i-j**2]+1)
print(d[N])