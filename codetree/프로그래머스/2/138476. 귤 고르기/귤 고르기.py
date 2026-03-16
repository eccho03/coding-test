from collections import Counter
def solution(k, tangerine):
    answer = 0
    
    cnt = Counter(tangerine)
    sorted_cnt = sorted(cnt.values(), reverse=True)
    
    # print(sorted_cnt)
    
    idx=0
    amount=0
    while True:
        if amount>=k:
            break
        amount+=sorted_cnt[idx] #현재 귤개수
        idx+=1;
        # print(amount)
    
    return idx