def solution(bandage, health, attacks):
    answer = 0
    time, x, y = bandage
    
    N = attacks[-1][0]
    streak = 0
    cur_heal = health
    
    att_idx = 0
    
    for i in range(1, N+1):
        att_time, att_amount = attacks[att_idx]
        # heal
        if att_time!=i:
            streak+=1
            cur_heal = min(health, cur_heal+x)
            #print(i, cur_heal)
        
        # 몬스터 공격
        else:
            streak=0 # 연속 성공 초기화
            cur_heal -= att_amount
            att_idx+=1
            #print(i, cur_heal)
            
            if cur_heal<=0:
                return -1
        
        
        if streak==time:
            cur_heal = min(health, cur_heal+y)
            #print("streak!", cur_heal)
            streak=0
    
    #print(cur_heal)
    
    if cur_heal<=0:
        return -1
    else:
        return cur_heal