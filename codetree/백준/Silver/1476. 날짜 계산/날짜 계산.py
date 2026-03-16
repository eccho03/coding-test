E, S, M = map(int, input().split())

if (E,S,M)==(1,1,1):
    print(1)
else:
    year = 1
    e, s, m = 1, 1, 1
    while True:
        year += 1
        e, s, m = e+1, s+1, m+1

        if e>15:
            e=1
        if s>28:
            s=1
        if m>19:
            m=1
        if (e,s,m)==(E,S,M):
            break
    print(year)