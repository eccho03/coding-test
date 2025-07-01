N = int(input())
d = [0]*(N+1)
d[0], d[1] = 1, 1

for i in range(2, N+1):
    d[i] = d[i-1] + d[i-2]

# print(d)

ans = [0]*(N+1)
for i in range(1,N+1):
    ans[i] = d[i-1]*2 + d[i]*2

print(ans[N])