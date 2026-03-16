def op_next(mm,ss, video_len):
    last_mm = int(video_len[:2])
    last_ss = int(video_len[3:])
    # 남은 시간10초 미만
    if (last_mm * 60 + last_ss) - (mm * 60 + ss) <= 10:
        mm, ss = last_mm, last_ss
    else:
        ss+=10
        if ss>=60:
            ss-=60
            mm+=1
    
    mm,ss = change_mm_ss(mm, ss)
        
    return mm, ss

def op_prev(mm, ss):
    # 현재 위치 10초 미만
    if mm==0 and ss<10:
        mm, ss = 0, 0
    else:
        ss-=10
        if ss<0:
            ss+=60
            mm-=1
            
    mm,ss = change_mm_ss(mm, ss)
        
    return mm, ss

def op_pass(op_start, op_end, pos, mm, ss):
    start_mm = int(op_start[:2])
    end_mm = int(op_end[:2])
    start_ss = int(op_start[3:])
    end_ss = int(op_end[3:])
    mm = int(pos[:2])
    ss = int(pos[3:])
    # print(start_mm, end_mm)
    # print(start_ss, end_ss)
    
    flag=False
    start_time = start_mm * 60 + start_ss
    end_time = end_mm * 60 + end_ss
    cur_time = mm * 60 + ss

    if start_time <= cur_time <= end_time:
        return op_end
    else:
        return pos


def change_mm_ss(mm, ss):
    if mm<10:
        mm = '0'+str(mm)
    else:
        mm = str(mm)
    if ss<10:
        ss = '0'+str(ss)
    else:
        ss = str(ss)
    
    return mm, ss
    

def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        mm = int(pos[:2])
        ss = int(pos[3:])
        pos = op_pass(op_start, op_end, pos, mm, ss)
        mm = int(pos[:2])
        ss = int(pos[3:])
        
        if command == "next":
            mm, ss = op_next(mm, ss, video_len)
        else:
            mm, ss = op_prev(mm, ss)
        pos = mm + ":" + ss

        pos = op_pass(op_start, op_end, pos, mm, ss)
        
    return pos