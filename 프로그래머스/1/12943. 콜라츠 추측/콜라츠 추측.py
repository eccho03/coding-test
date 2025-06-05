def solution(num):
    answer = 0
    
    if num==1:
        return 0
    
    while True:
        answer += 1 # 작업 횟수
        
        if num%2==0:
            num/=2
        else:
            num=num*3+1
        
        if num==1:
            break
        if answer>=500:
            answer = -1
            break
    
    return answer