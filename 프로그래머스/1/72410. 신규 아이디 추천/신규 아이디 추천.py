def solution(new_id):
    answer = ''
    dot_flag=False
        
    for idx, ch in enumerate(new_id):        
        if ch.isupper():
            answer+=ch.lower()
            continue
            
        if ch.islower() or ch.isdigit() or ch in ('-','_','.'):
            answer+=ch
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    answer = answer.lstrip('.')
    answer = answer.rstrip('.')
            
    if len(answer)==0:
        answer = 'a'
    
    if len(answer)>=16:
        answer = answer[:15].rstrip('.')
        
    if len(answer)<=2:
        while True:
            last = answer[-1]
            answer+=last
            if len(answer)==3: break
    
    return answer