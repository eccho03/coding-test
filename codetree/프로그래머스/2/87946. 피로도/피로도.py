from itertools import permutations

def solution(k, dungeons):
    def find_dungeons(orders, k):
        cur_k = k
        cnt = 0
        
        for idx in orders:
            idx = idx-1 # change to 0-based
            cur_dungeon = dungeons[idx]
            
            if cur_k >= cur_dungeon[0]:
                # 최소 필요 피로도 이상인 경우 - 탐험 가능
                cur_k -= cur_dungeon[1]
            else:
                break
            cnt += 1
        
        return cnt
            
    
    answer = -1
    N = len(dungeons)
    rounds = [i for i in range(1, N+1)]
    
    mx_cnt = 0
    for i in permutations(rounds, N):
        cnt = find_dungeons(i, k)    # i 순서대로 던전 탐색
        mx_cnt = max(mx_cnt, cnt)

    return mx_cnt