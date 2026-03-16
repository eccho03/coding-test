from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    
    N = len(enroll)
    parent={}
    
    for i in range(N):
        parent[enroll[i]] = referral[i]
    
    # print(graph)
    
    enroll_amounts = {}
    for i in range(N):
        enroll_amounts[enroll[i]]=0
    enroll_amounts['-']=0
    
    M = len(seller)
    
    for i in range(M):
        cur_money = amount[i]*100
        cur_node = seller[i]
        while cur_node!="-" and cur_money>0:
            give = cur_money//10
            keep = cur_money-cur_money//10
            enroll_amounts[cur_node] += keep
            cur_node = parent[cur_node]
            cur_money = give
            
    for num in enroll_amounts.values():
        answer.append(num)
    answer.pop()
    # print(parent)
    # print(enroll_amounts)
    
    return answer