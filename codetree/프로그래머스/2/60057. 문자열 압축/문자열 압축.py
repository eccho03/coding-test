def solution(s):
    answer = float('inf')
    length = len(s)
    
    for token in range(1, length//2 + 1):
        compressed = ""
        word_cnt = 1
        prev = s[:token]
        
        for i in range(token, length, token):
            if s[i:i+token] == prev:
                word_cnt += 1
            else:
                compressed += (str(word_cnt) + prev) if word_cnt > 1 else prev
                prev = s[i:i+token]
                word_cnt = 1
        
        compressed += (str(word_cnt) + prev) if word_cnt > 1 else prev
        answer = min(answer, len(compressed))
    return answer if length > 1 else 1

# while문보다는 for문을 떠올려보기 -> 범위가 어디서부터 어디일까를 먼저 고민
# 길이가 1일 때 따로 고려
# 전체를 계속 비교하는 것보다 prev를 두는 방법 사용
