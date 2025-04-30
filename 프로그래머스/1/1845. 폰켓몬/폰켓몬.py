from collections import Counter
def solution(nums):
    choose_cnt = len(nums)//2 # 골라야 하는 폰켓몬 개수
    cnt_nums = Counter(nums)
    #print(cnt_nums)
    
    answer = 0
    
    for key,val in cnt_nums.items():
        val-=1
        choose_cnt-=1
        #print(key,val)
        answer+=1
        if choose_cnt<=0:
            break
    return answer