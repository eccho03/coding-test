N, K = map(int, input().split())
lst = []
i = 1
for i in range(1,N+1):
    if N%i==0:
        lst.append(i)
        K-=1
        if K==0:
            break

# print(K)
# print(i)

if K!=0:
    print(0)
else:
    print(i)