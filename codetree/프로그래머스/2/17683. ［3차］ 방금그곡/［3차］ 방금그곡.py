def solution(m, musicinfos):
    answer = ''
    target = []
    
    init = []
    idx=0
    while True:
        if idx>=len(m):
            break
        tmp=m[idx]
        if idx< len(m)-1 and not m[idx+1].isalpha():
            tmp+=m[idx+1]
            idx+=1
        init.append(tmp)
        idx+=1
    
    init = str(init)
    
    for musicinfo in musicinfos:
        melody = []
        idx=0
        
        cur_music = musicinfo.split(",")
        start_mm, start_ss = cur_music[0].split(":")
        end_mm, end_ss = cur_music[1].split(":")
        if int(end_ss)-int(start_ss)>=0:
            length = int(end_ss)-int(start_ss)
            length += (int(end_mm)-int(start_mm))*60
        else:
            length = (int(end_mm)-int(start_mm))*60
            length += int(end_ss)-int(start_ss)+60
            length -= 60

        cnt=0
        N=len(cur_music[3])
        while True:
            if cnt>=length:
                break
            cnt+=1
            tmp=cur_music[3][idx%N]
            if not cur_music[3][(idx+1)%N].isalpha():
                tmp+=cur_music[3][(idx+1)%N]
                idx=(idx+1)%N
            melody.append(tmp)
            idx+=1

        cur_melody = str(melody)
        target.append((cur_music[2], cur_melody, length))
        # print(cur_melody)

    target.sort(key=lambda x: x[2], reverse=True)
    for target_name, target_melody, _ in target:
        # print(init, target_melody)
        if init[1:-1] in target_melody:
            return target_name
    
    return "(None)"