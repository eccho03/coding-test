def solution(keymap, targets):
    answer = []
    INF = float('inf')
    
    def find_target(key, target):
        for i in range(len(key)):
            if key[i]==target:
                return i
        return -1
    
    for target in targets:
        cur_target_mn_idx = 0
        for i in range(len(target)):
            mn_idx = INF
            for cur_key in keymap:
                idx = find_target(cur_key, target[i])
                if idx!=-1:
                    mn_idx = min(mn_idx, idx)
            cur_target_mn_idx+=mn_idx+1
            
        if cur_target_mn_idx==INF:
            answer.append(-1)
        else:
            answer.append(cur_target_mn_idx)
    
    return answer