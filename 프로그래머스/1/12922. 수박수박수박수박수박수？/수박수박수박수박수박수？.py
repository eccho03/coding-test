def solution(n):
    answer = ''
    
    for i in range(n):
        if i%2==0:#짝수
            answer+="수"
        else:
            answer+="박"
            
    return answer