def solution(board, moves):
    answer = 0
    N = len(board[0])
    stack = []
        
    def find_target(line):
        for i in range(N):
            # print(board[i][line])
            if board[i][line]!=0:
                return i, board[i][line]
        return -1,-1
    
    for m in moves:
        idx, doll = find_target(m-1)
        if idx==-1: continue
        
        board[idx][m-1]=0
        stack.append(doll)
        # print(stack)
        
        if len(stack)>=2:
            if stack[-1]==stack[-2]:
                stack.pop()
                stack.pop()
                answer+=2
        
        # print("-----------------")
    return answer