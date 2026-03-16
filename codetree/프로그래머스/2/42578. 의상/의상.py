from collections import defaultdict

def solution(clothes):
    answer = 1
    day = defaultdict(list)

    for name, typ in clothes:
        day[typ].append(name)

    # print(day)
        
    for name, typ in day.items():
        # print(name, typ)
        tmp = len(typ) +1
        answer *= tmp

    return answer-1
