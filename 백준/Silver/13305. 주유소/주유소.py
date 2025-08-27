N = int(input())
dist = list(map(int, input().split()))
amount = list(map(int, input().split()))

# (2+3+1)*5=30
# 2*5+(3+1)*2=18
# 2*5+3*2+1*4=20
cur_mn_amount=amount[0]
ans=0
for i in range(N-1):
    if cur_mn_amount>amount[i]:
        cur_mn_amount=amount[i]
    ans+=cur_mn_amount*dist[i]

print(ans)
