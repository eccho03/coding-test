def solution(board, moves):
    answer = 0
    N = len(board)
    
    def find_target(idx):
        for col in range(N):
            # print(board[col][idx])
            if board[col][idx]!=0:
                return board[col][idx], col
        return 0, 0
    
    basket = []
    
    for move in moves:
        target, col = find_target(move-1) # 0-based
        if target==0:   continue
        board[col][move-1]=0
        basket.append(target)
        if len(basket)>=2:
            if basket[-1]==basket[-2]:
                basket.pop(-1)
                basket.pop(-1)
                answer+=2
        # print(basket)
        
    
    return answer