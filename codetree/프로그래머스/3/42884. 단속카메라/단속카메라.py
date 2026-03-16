def solution(routes):
    answer = 0
    INF = float('inf')
    
    routes.sort(key=lambda x: x[1])
    # print(routes)
    
    camera = -INF
    
    for start, end in routes:
        if start>camera:
            camera=end
            answer+=1
    
    return answer