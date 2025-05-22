def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        start_hour, start_min = schedules[i]//100, schedules[i]%100
        
        #print("start: ",start_hour, start_min)
        end_hour, end_min = start_hour, start_min+10
        
        if end_min > 59:
            end_hour += end_min//60
            end_min = end_min%60
        
        #print("end: ",end_hour, end_min)
        
        flag = 0
        
        for j in range(7):
            if (startday+j)%7==0 or (startday+j)%7==6:
                continue
            cur_hour, cur_min = timelogs[i][j]//100, timelogs[i][j]%100
            
            if cur_hour<end_hour or (cur_hour==end_hour and cur_min<=end_min):
                pass
            else:
                flag = 1
                break
        if flag==0:
            #print(f'{i+1}번째 사람 지각 안 함')
            answer += 1
    
    return answer