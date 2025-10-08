from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    results = set()
    
    def check(cur_user_id, cur_banned_id):
        if len(cur_user_id)!=len(cur_banned_id):
            return False
        for i in range(len(cur_user_id)):
            if not (cur_user_id[i]==cur_banned_id[i] or cur_banned_id[i]=='*'):
                return False
        return True
        
    
    for permu in permutations(user_id, len(banned_id)):
        # print(permu)
        flags = []
        for user, banned in zip(permu, banned_id):
            flags.append(1 if check(user, banned) else 0)
        if all(f==1 for f in flags): results.add(tuple(sorted(permu)))
    
    return len(results)