import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)
    cnt=0
    while len(scoville)>1:
        cur = heapq.heappop(scoville)
        if cur < K:
            nxt = heapq.heappop(scoville)
            mix = cur + (nxt*2)
            # print(nxt, mix)
            heapq.heappush(scoville, mix)
        else:
            break
        # print(scoville)
        cnt+=1
    
    if scoville:
        mn_scoville = heapq.heappop(scoville)
        if mn_scoville>=K:
            answer = cnt
        else:
            answer = -1
    else:
        answer = cnt
        
    
    return answer