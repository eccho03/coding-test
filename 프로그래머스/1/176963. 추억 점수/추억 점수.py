def solution(name, yearning, photo):
    answer = []
    
    for ph in photo:
        tmp_sum = 0
        for person in ph:
            if person not in name: continue
            tmp_sum += yearning[name.index(person)]
        answer.append(tmp_sum)
    return answer