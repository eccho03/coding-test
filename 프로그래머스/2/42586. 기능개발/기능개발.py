def solution(progresses, speeds):
    answer = []
    day = 0
    idx = 0
    q = []
    flags = [0]*len(progresses)
    
    while not all(progress >= 100 for progress in progresses):
        day += 1
        today = []
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
            if progresses[i] >= 100 and i not in q:
                q.append(i)
        
        # print(q)
        
        for num in q:
            if all(i in q for i in range(num)) and flags[num]==0:
                today.append(num)
                flags[num]=1
        
        if len(today)>0:
            answer.append(len(today))
    
    #print(day)
    
    return answer