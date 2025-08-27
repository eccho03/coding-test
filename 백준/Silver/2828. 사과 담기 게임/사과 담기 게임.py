N, length = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

si,sj=1,length
ans=0
for loc in apples:
    if sj<loc:
        ans+=loc-sj
        si+=loc-sj
        sj=si+(length-1)
    elif si>loc:
        ans+=si-loc
        sj-=si-loc
        si=sj-(length-1)

    # print(si,sj)

print(ans)