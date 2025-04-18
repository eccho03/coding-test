N = int(input())
d = [[0] * (N+1) for _ in range(N+1)]

d[1][0] = 0
d[1][1] = 1

for i in range(2, N+1):
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]
print(d[N][0]+d[N][1])