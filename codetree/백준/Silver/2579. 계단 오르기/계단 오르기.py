N = int(input())
stairs = []
for _ in range(N):
    num = int(input())
    stairs.append(num)

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
else:
    d = [0] * N
    d[0] = stairs[0]
    d[1] = stairs[0] + stairs[1]
    d[2] = max(stairs[1] + stairs[2], d[0] + stairs[2])
    
    for i in range(3,N):
        d[i]=max(d[i-2]+stairs[i],d[i-3]+stairs[i-1]+stairs[i])
    print(d[N-1])