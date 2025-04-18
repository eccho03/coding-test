N = int(input())
d = [0 for _ in range(91)]

d[0]=0
d[1]=1

for i in range(2, N+1):
    d[i]=d[i-1]+d[i-2]
print(d[N])