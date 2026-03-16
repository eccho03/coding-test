i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    first = (V // P) * L 
    second = V % P
    if second > L:
        second = L
    result = first + second
    print("Case %d: %d" % (i, result))
    i += 1
