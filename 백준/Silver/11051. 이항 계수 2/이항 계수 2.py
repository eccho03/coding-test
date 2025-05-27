N, K = map(int, input().split())

if K==0:
    print(1)
elif K==1:
    print(N)
else:
    if 2*K>N:
        K = N-K
    d = [1] * (N+1)
    d[0] = N

    for i in range(1, K):
        d[i] = d[i-1] * (N-i)

    k = [1] * (K+1)

    for i in range(2, K+1):
        k[i] = k[i-1] * i

    #print(k)
    print((d[K-1]//k[K])%10_007)