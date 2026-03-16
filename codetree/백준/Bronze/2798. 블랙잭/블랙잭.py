from itertools import combinations

N,M = map(int,input().split())
num = list(map(int, input().split()))
ans = 0
for i in combinations(num, 3):
    tlst = list(i)
    #print(sum(tlst))

    if sum(tlst) <= M:
        if ans < sum(tlst):
            ans = sum(tlst)

print(ans)
