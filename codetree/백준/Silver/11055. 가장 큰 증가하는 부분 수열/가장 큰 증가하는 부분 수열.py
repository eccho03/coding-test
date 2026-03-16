N = int(input())
A = list(map(int, input().split()))
# print(A)

d = [0]*(N+1)
d = A[:]

ans = 0
for i in range(1,N):
    for j in range(i):
        tmp=0
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + A[i])

print(max(d))