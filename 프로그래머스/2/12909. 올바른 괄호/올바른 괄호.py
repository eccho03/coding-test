def solution(s):
    
    def is_empty(stack):
        if len(stack)<=0:   return True
        return False
    
    stack = []
    N = len(s)
    flag = True
    
    for num in s:
        if num=='(':
            stack.append(num)
        else:
            if is_empty(stack):
                return False
            top = stack[-1]
            if top=='(':
                stack.pop(-1)
        
        #print(stack)
    
    if len(stack)==0:
        return True
    else:
        return False