N,P,Q = map(int,input().split())
strawberry = list(map(int,input().split()))
grape = list(map(int,input().split()))

flag = 0
# 1초마다 진행
i = 0
cnt = [0] * N

for i in range(N):
    for _ in range(10001):

        if strawberry[i]==grape[i]:
            break
        strawberry[i] += P
        grape[i] += Q
        cnt[i]+=1

for i in range(N):
    if cnt[i]>10000:
        flag=1

if flag==1:
    print("NO")
else:
    print("YES")
    print(*cnt)