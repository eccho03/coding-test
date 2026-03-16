N=int(input())
S=list(map(int, input().split()))
d=[-1001] * 100001
d[0]=S[0]

for i in range(1,N):
    d[i]=max(d[i-1]+S[i],S[i])

print(max(d))