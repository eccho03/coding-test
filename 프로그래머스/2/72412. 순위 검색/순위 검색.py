from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    hashMap = defaultdict(list)
    
    for cur_info in info:
        token = cur_info.split(" ")
        score = int(token[-1])
        conditions = token[:-1]
        # print(conditions)
        
        for n in range(5):
            for c in combinations(range(4), n):
                tmp = [x[:] for x in conditions]
                for i in c:
                    tmp[i] = '-'
                key = ' '.join(tmp)
                hashMap[key].append(score)
        
    
    for k in hashMap:
        hashMap[k].sort()

    # print(hashMap)
    
    for q in query:
        q = q.split(" and ")
        tmp = q.pop(-1).split(" ")
        q += tmp
        
        score = int(q[-1])
        q = q[:-1]
        key = ' '.join(q)
        # print(q)

        if key in hashMap:
            scores = hashMap[key]
            idx = bisect.bisect_left(scores, score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
        
    
    
    return answer