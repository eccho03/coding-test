def solution(name):
    answer = 0
    flag=[1]*len(name)
    
    for i in range(len(name)):
        if name[i]=='A':
            flag[i]=0
    
    for ch in name:
        front, back = ord(ch)-ord('A'), ord('Z')-ord(ch)+1
        answer += min(front, back)
        #print(front, back)
    # print(answer)
    
    min_move = len(name) - 1

    for i in range(len(name)):
        next_idx = i + 1

        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        move = i + len(name) - next_idx + min(i, len(name) - next_idx)
        min_move = min(min_move, move)

    answer += min_move
    
    return answer