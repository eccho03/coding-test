def is_correct(s):
    N = len(s)
    stack = []
    
    for ch in s:
        if ch=='(':
            stack.append(ch)
        else:
            if stack and stack[-1]=='(':
                stack.pop(-1)
            else:
                return False
            
    if stack:
        return False
    else:
        return True

def is_balance(s):
    cnt1, cnt2 = 0, 0
    
    for ch in s:
        if ch=='(':
            cnt1+=1
        else:
            cnt2+=1
    
    if cnt1==cnt2:
        return True
    else:
        return False

def oper_reverse(s):
    new_s = ''
    for ch in s:
        if ch=='(':
            new_s+=')'
        else:
            new_s+='('
            
    return new_s

def get_solution(p):
    # print("p:",p)
    # 1
    if p=='':   
        return ''

    # 2
    u, v = '', ''
    for i in range(1, len(p)):
        if is_balance(p[:i]) and is_balance(p[i:]):
            u, v = p[:i], p[i:]
            break
    if u=='':
        u = p

    # print(f'u: {u}, v: {v}')

    if is_correct(u):
        return u + get_solution(v)
    else:
        tmp = '('
        tmp += get_solution(v)
        tmp += ')'
        return tmp + oper_reverse(u[1:-1])
    
def solution(p):
    if is_correct(p):
        answer = p
    else:
        answer = get_solution(p)    
    
    return answer