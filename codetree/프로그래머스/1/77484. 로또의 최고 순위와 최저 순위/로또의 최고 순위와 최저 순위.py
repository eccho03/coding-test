def solution(lottos, win_nums):
    answer = []
    same_cnt = 0 # 일치하는 번호 개수
    not_cnt = 0 # 모르는 번호 개수
    
    prize = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for num in lottos:
        if num in win_nums:
            same_cnt += 1
        elif num==0:
            not_cnt += 1
    
    
    return [prize[same_cnt+not_cnt], prize[same_cnt]]