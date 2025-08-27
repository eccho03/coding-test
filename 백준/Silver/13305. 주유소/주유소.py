N = int(input())
dist = list(map(int, input().split()))
amount = list(map(int, input().split()))

# (2+3+1)*5=30
# 2*5+(3+1)*2=18
# 2*5+3*2+1*4=20
cur_amount=0
for i in range(N-1):
    cur_mn_amount = min(amount[i:N-1])
    # print(cur_mn_amount)

    if amount[i]==cur_mn_amount:
        cur_amount+=sum(dist[i:])*amount[i]
        break
    else:
        cur_amount+=dist[i]*amount[i]

print(cur_amount)
