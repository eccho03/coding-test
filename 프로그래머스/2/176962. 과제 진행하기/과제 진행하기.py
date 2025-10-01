def solution(plans):
    answer = []
    
    def add_time(hh1, mm1, hh2, mm2):
        hh1, mm1, hh2, mm2 = int(hh1), int(mm1), int(hh2), int(mm2)
        cur_hh, cur_mm = hh1+hh2, 0
        if mm1+mm2>=60:
            cur_mm = mm1+mm2-60
            cur_hh+=1
        else:
            cur_mm = mm1+mm2
        if cur_hh>=24:
            cur_hh-=24
        
        return cur_hh*60+cur_mm
            
    
    def sub_time(hh1, mm1, hh2, mm2):
        hh1, mm1, hh2, mm2 = int(hh1), int(mm1), int(hh2), int(mm2)
        cur_hh, cur_mm = hh2-hh1, 0
        if mm2-mm1>=0:
            cur_mm = mm2-mm1
        else:
            cur_hh -= 1
            cur_mm = mm2-mm1+60
        
        return cur_hh*60+cur_mm
    
    plans.sort(key=lambda x: x[1]) #시작하는 시간 빠른 순
    q = []
    
    def operation(cur_start, cur_playtime, nxt_start):
        
        cur_hh, cur_mm = cur_start.split(":")
        nxt_hh, nxt_mm = nxt_start.split(":")
        
        res_time = sub_time(cur_hh, cur_mm, nxt_hh, nxt_mm)
                
        return res_time, int(cur_playtime)
        
    idx=0
        
    while idx<len(plans)-1:
        cur_name, cur_start, cur_playtime = plans[idx]
        nxt_name, nxt_start, nxt_playtime = plans[idx+1]
        res_time, remain_time = operation(cur_start, cur_playtime, nxt_start)
        
        # if q:
        #     print(cur_name, q)
        # else:
        #     print(cur_name, "[ ]")
        
        if res_time >= remain_time:
            answer.append(cur_name)
            left_time = res_time - remain_time
            
            while left_time > 0 and q:
                cur_name, cur_start, cur_playtime = q.pop()
                if left_time>= cur_playtime:
                    answer.append(cur_name)
                    left_time -= cur_playtime
                else:
                    q.append((cur_name, cur_start, abs(cur_playtime - left_time)))
                    left_time = 0
                
                
                # print(cur_name, q)
                # print(cur_playtime, nxt_playtime)                

                
        else:
            left_time = remain_time - res_time
            q.append((cur_name, cur_start, left_time))
        
        idx+=1
        
    
    answer.append(plans[-1][0])
    while q:
        cur_name, _, _ = q.pop(-1)
        answer.append(cur_name)
    
#     hh, mm = sub_time(11,40,12,10)
#     print(hh, mm)
    
#     hh, mm = add_time(11,50,12,10)
#     print(hh, mm)    
    
    return answer