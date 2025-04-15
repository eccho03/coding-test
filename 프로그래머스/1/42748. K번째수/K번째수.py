def solution(array, commands):
    answer = []
    
    for c in commands:
        i,j,k=c  # i~j번째 자르기 / 배열의 k번째 숫자
        token = array[i-1:j]
        token.sort()
        answer.append(token[k-1])
    
    return answer