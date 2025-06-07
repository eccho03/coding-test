def can_use(S):
    global a,c,g,t
    for i in S:
        if i=='A':
            a += 1
        elif i=='C':
            c += 1
        elif i=='G':
            g += 1
        elif i=='T':
            t += 1

    return a, c, g, t


def check():
    if a >= a_cnt and c >= c_cnt and g >= g_cnt and t >= t_cnt:
        return True
    else:
        return False


S, P = map(int, input().split())
dna = input()
a_cnt, c_cnt, g_cnt, t_cnt = map(int, input().split())

a = c = g = t = 0

# print(dna)
# print(a_cnt, c_cnt, g_cnt, t_cnt)

ans = 0
a,c,g,t = can_use(dna[:P])
if check():
    ans += 1

for i in range(P, S):
    # print(dna[i:i+P])
    prev = dna[i-P] # 빠지는 문자

    if prev == 'A':
        a-=1
    elif prev == 'C':
        c-=1
    elif prev == 'G':
        g-=1
    elif prev == 'T':
        t-=1

    new = dna[i] # 새로 들어오는 문자
    if new == 'A':
        a += 1
    elif new == 'C':
        c += 1
    elif new == 'G':
        g += 1
    elif new == 'T':
        t += 1

    if check():
        ans += 1

print(ans)