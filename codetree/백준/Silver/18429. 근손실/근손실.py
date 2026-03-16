# 하루가 지날때마다 중량 K씩 감소
# N개의 운동키트
# 1~N일차 항상 중량 500 이상이어야 함

def check(orders):
    cur_weight = 500
    for i in range(N):
        cur_kit = kit[orders[i]-1]
        cur_weight -= K
        cur_weight += cur_kit
        #print(cur_kit)
        if cur_weight < 500:
            return False
    return True



from itertools import permutations

N, K = map(int, input().split())
kit = list(map(int, input().split()))
days = [i for i in range(1,N+1)]

cnt=0
for i in permutations(days, N):
    if check(i):
        cnt+=1

print(cnt)
