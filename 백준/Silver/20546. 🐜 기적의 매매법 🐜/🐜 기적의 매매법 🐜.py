M = int(input()) # 현금
machine = list(map(int, input().split())) # 주가

a_money,b_money = M,M # A: 준현, B: 성민 남은 금액
a_cnt, b_cnt = 0,0    # 가지고 있는 주식 수

def total_amount(money, cnt):
    return money+machine[-1]*cnt

for i in range(len(machine)):
    status = machine[i] # i일차 주가

    # 남은 잔액이 없거나 가지고 있는 돈보다 주가가 높을 때
    if a_money<=0 or a_money<status:
        continue

    # 준현: 현금 내에서 전량 매수
    while a_money>0:
        a_money -= status
        # if a_money <= 0:
        #     a_money += status
        #     break
        a_cnt+=1

for i in range(3,len(machine)):
    # 성민 - 1) 3일 연속 상승=>전량 매도 2) 3일 연속 하락=>전량 매수
    m1,m2,m3 = machine[i-3], machine[i-2], machine[i-1]
    status = machine[i]

    # 2-1) 3일 연속 상승
    if m1<m2<m3:
        if b_cnt<=0:
            continue
        while b_cnt>0:
            b_money += status
            b_cnt-=1

    # 2-2) 3일 연속 하락
    if m1>m2>m3:
        #print(i, b_cnt, b_money)
        while b_money > 0:
            b_money -= status

            if b_money < 0:
                b_money += status
                break
            b_cnt += 1

ans1 = total_amount(a_money, a_cnt)
ans2 = total_amount(b_money, b_cnt)
# # print(ans1, ans2)
if ans1>ans2:
    print("BNP")
elif ans1<ans2:
    print("TIMING")
else:
    print("SAMESAME")