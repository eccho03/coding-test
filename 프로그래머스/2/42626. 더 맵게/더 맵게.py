import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville)>=2:
    
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        # print(scoville)
        
        if first>=K:
            return answer
        
        heapq.heappush(scoville, first+second*2)
        
        answer+=1
    
    if min(scoville)>=K:
        return answer
    else:
        return -1