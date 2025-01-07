T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = [1] * (n + 1)
    b = [1] * (n + 1)

    for i in range(1, n + 1):
        a[i] = (m-i+1) * a[i-1]
    for i in range(1, n + 1):
        b[i] = i * b[i-1]

    print(a[n]//b[n])
