score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
mytype = {'R':0, 'T':0, 'C':0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

def solution(survey, choices):
    answer = ''
    
    size = len(survey)
    
    for pair in zip(survey, choices):
        find, choice = pair
        start, end = find
        
        #print(start, end, choice)
        
        if choice<4:
            mytype[start]+=score[choice]
        else:
            mytype[end]+=score[choice]
    
    if mytype['R'] < mytype['T']:
        answer += 'T'
    else:
        answer += 'R'
        
    if mytype['C'] < mytype['F']:
        answer += 'F'
    else:
        answer += 'C'
    
    if mytype['J'] < mytype['M']:
        answer += 'M'
    else:
        answer += 'J'
    
    if mytype['A'] < mytype['N']:
        answer += 'N'
    else:
        answer += 'A'
    
    
    return answer