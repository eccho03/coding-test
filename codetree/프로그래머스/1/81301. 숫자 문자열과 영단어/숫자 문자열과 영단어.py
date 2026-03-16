def solution(s):
    answers = []
    answer = ''
    num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    tmp = ''
    
    for i in range(len(s)):
        if tmp in num.keys():
            answers.append(num[tmp])
            tmp = ''
        
        if not s[i].isalpha():
            answers.append(int(s[i]))
        else:
            tmp += s[i]
    
    if tmp in num.keys():
        answers.append(num[tmp])
        
    return int(''.join(map(str, answers)))