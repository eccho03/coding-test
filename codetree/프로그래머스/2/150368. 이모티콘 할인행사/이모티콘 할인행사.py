from itertools import product

def solution(users, emoticons):
    answer = []
    
    # 1. 이모티콘 플러스 서비스 가입자 늘리기
    # 2. 이모티콘 판매액 늘리기
    # 할인율 10/20/30/40%
    discount = [0.1,0.2,0.3,0.4]
    N, M = len(users), len(emoticons)
    
    
    for i in product(discount, repeat=M):
        lst = list(i)
        # print(m)
        cnt_plus = 0
        total_money = 0
        # print(lst)
        for n in range(N):
            cur_emoticon_money = 0
            for m in range(M):
                if users[n][0]<=lst[m]*100:
                    cur_emoticon_money += emoticons[m]*(1-lst[m])
            
            if cur_emoticon_money>=users[n][1]:
                cnt_plus += 1
                cur_emoticon_money = 0
            total_money+=cur_emoticon_money
                
        answer.append((cnt_plus, total_money))
    
    answer.sort(reverse=True)
    # print(answer)
    
    return answer[0]