T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    d = [[0] * n for _ in range(k)]
    for i in range(n):
        d[0][i] = i + 1

    for i in range(1, k):
        for j in range(n):  
            d[i][j] = sum(d[i-1][:j+1])
    print(sum(d[k-1]))