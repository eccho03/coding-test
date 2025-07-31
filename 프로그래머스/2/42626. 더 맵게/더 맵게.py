import heapq

def solution(scoville, K):
    answer = 0
    N = len(scoville)
    heapq.heapify(scoville)
    
    while len(scoville)>1:
        mn_scov_first = heapq.heappop(scoville)
        mn_scov_second = heapq.heappop(scoville)
        
        if mn_scov_first >= K or answer>=N-1:
            break
        
        mixed_scov = mn_scov_first + (mn_scov_second*2)
        heapq.heappush(scoville, mixed_scov)
            
        answer+=1
        # print(scoville)
    
    for i in range(len(scoville)):
        if scoville[i]<K:
            return -1
        
    
    return answer