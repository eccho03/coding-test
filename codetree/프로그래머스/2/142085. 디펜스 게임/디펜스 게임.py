def solution(n, k, enemy):
    answer = 0
    
    start, end = 0, len(enemy)
    
    def is_alive(target, n):
        sorted_target = sorted(target, reverse = True)
        
        for i in range(len(target)):
            if i < k:
                continue    # 무족권 사용
            if n < sorted_target[i]:
                return False
            
            n-=sorted_target[i]
        
        return True
            
    
    while start <= end:
        mid = (start+end)//2
        
        if is_alive(enemy[:mid], n):
            start = mid+1 # 살아남았으면 더 많은 라운드를 살아남을 수 있는지 확인
            answer = mid
            
        else:
            end = mid-1
            
    return answer