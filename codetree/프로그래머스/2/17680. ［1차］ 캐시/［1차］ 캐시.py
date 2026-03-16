def solution(cacheSize, cities):
    answer = 0
    
    q = []
    if cacheSize==0:
        answer = len(cities)*5
        return answer
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in q:
            # cach hit
            answer+=1
            q.remove(cities[i])
            q.append(cities[i])
        else:
            if len(q)<cacheSize:
                # cache miss
                answer+=5
                q.append(cities[i])
            else:
                # cache miss
                answer+=5
                q.pop(0)
                q.append(cities[i])
                
        # print(answer)
        # print(q)
            
    
    return answer