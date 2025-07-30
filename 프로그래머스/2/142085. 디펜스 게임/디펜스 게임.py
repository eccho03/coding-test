def solution(n, k, enemy):
    answer = 0
    rounds = len(enemy)
    
    start, end = 0, rounds
    
    def check(mid, n, k):
        cur = enemy[:mid]
        target = sorted(cur, reverse=True)
        # print(enemy[:mid])
        # print(target)

        for i in range(mid):
            if i < k:
                continue  # 무적권 사용
            if target[i] > n:
                return False
            n -= target[i]
        return True
      
    
    while start <= end:
        mid = (start+end)//2
        
        if check(mid, n, k):
            start = mid+1
            answer = mid
        else:
            end = mid-1

    return answer