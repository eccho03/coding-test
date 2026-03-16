import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(heap, (time, i + 1))
    
    ate = 0
    prev = 0

    length = len(food_times)
    while heap and (heap[0][0] - prev) * length <= k:
        cur_time, idx = heapq.heappop(heap)
        k -= (cur_time - prev) * length
        ate = cur_time
        length -= 1
        prev = cur_time
    
    heap.sort(key=lambda x: x[1])
    answer = heap[k % length][1]
        
    return answer