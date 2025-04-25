def solution(people, limit):
    answer = 0
    people.sort()
    
    left_idx=0
    right_idx=len(people)-1
    rescue_cnt = 0
    
    while left_idx<=right_idx:
        
        if people[left_idx]+people[right_idx]<=limit:
            left_idx+=1
        right_idx-=1
        rescue_cnt+=1
        
    answer = rescue_cnt
    
    return answer