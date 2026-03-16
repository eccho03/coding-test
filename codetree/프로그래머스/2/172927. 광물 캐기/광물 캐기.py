from itertools import permutations
def solution(picks, minerals):
    answer = 0
    mapping = {"diamond": 0, "iron": 1, "stone": 2}
    
    tired = [[1,1,1],[5,1,1],[25,5,1]]
    
    target = []
    for i in range(0, len(minerals), 5):
        if len(target) == sum(picks):
            break
        target.append(minerals[i:i+5])
    
    # print(target)
    
    scores = []
    for t in target:
        score = sum(tired[2][mapping[m]] for m in t)
        scores.append((score, t))
    
    scores.sort(reverse=True, key=lambda x: x[0])
    # print(scores)
    
    pick_order = []
    for i, cnt in enumerate(picks):
        pick_order += [i]*cnt
    
    # print(pick_order)
    
    for idx, (score, cur_group) in enumerate(scores):
        if idx>=len(pick_order):
            break
        cur_pick = pick_order[idx]
        for g in cur_group:
            answer += tired[cur_pick][mapping[g]]
    
    return answer