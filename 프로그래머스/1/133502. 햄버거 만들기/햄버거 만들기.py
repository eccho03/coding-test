def solution(ingredient):
    answer = 0
    
    stack = []
    
    for num in ingredient:
        stack.append(num)
        if len(stack)>=4:
            if (stack[-4],stack[-3],stack[-2],stack[-1])==(1,2,3,1):
                stack.pop(-1)
                stack.pop(-1)
                stack.pop(-1)
                stack.pop(-1)
                answer+=1

    
    return answer