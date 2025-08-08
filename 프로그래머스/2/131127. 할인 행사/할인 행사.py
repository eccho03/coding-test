from collections import defaultdict
def solution(want, number, discount):
    def check(start, end):
        want_cnt = defaultdict(int)
        dis_cnt = defaultdict(int)
        for i in range(start, end+1):
            dis_cnt[discount[i]]+=1
        for i in range(len(want)):
            want_cnt[want[i]]+=number[i]
        
        # print(dis_cnt, want_cnt)
        if dis_cnt==want_cnt:
            return True
        else:
            return False
    
    answer = 0
    start, end = 0, 9
    
    for i in range(len(discount)):
        if check(start, end):
            answer+=1
        start+=1
        end+=1
        if end>=len(discount):
            break
    
    return answer