N=int(input())
d = [[0,0] for _ in range(N+1)]
d[0][0] = 1
d[0][1] = 3

turn = {0:"SK",1:"CY"}
for i in range(1,N+1):
    t = turn[i%2]
    d[i][0] += d[i-1][0]+1
    d[i][1] += d[i-1][1]+3

print(t)

