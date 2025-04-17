def solution(s):
    answer = True
    
    for i in range(len(s)):
        if s[i] not in "1234567890":
            answer = False
            break
    if len(s)!=4 and len(s)!=6:
        answer = False
    
    return answer