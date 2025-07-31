from collections import defaultdict

def solution(gems):
    N = len(gems) # gems 크기
    M = len(set(gems))  # 보석 개수
    answer = [0, N-1]
    
    start, end = 0, 0
    gems_cnt = defaultdict(int)
    
    gems_cnt[gems[0]] = 1
    
    while end < N:
        if len(gems_cnt) < M:
            end += 1
            if end == N:
                break
            gems_cnt[gems[end]] += 1
        else:
            if end-start < answer[1]-answer[0]:
                answer = [start, end]
            
            gems_cnt[gems[start]]-=1
            if gems_cnt[gems[start]]==0:
                del gems_cnt[gems[start]]
            start += 1
    
    answer = [answer[0]+1, answer[1]+1]
    
    return answer