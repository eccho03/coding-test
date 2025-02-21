from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    
    # 원형 -> 선형 weak 확장
    weak = weak + [w + n for w in weak]

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            cover_range = weak[start] + friends[cnt - 1] # 가장 앞 취약 지점 + 커버 범위
            
            for i in range(start, start + length): 
                if cover_range < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    cover_range = weak[i] + friends[cnt - 1]
                    
            answer = min(answer, cnt)
    
    if answer > len(dist):
        answer = -1
    return answer