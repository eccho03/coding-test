from collections import Counter
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    part_cnt = Counter(participant)
    comp_cnt = Counter(completion)
    answer = (part_cnt- comp_cnt)
    
    return list(answer.keys())[0]