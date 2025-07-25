from collections import deque
def solution(game_board, table):
    answer = -1
    N = len(game_board)
    M = 6
    
    def find_answer():
        v = [0]*len(blocks)
        answer = 0

        for possible_loc in boards:
            si, sj = find_si_sj(possible_loc)
            norm_place = make_block(possible_loc)

            matched = False
            for idx, block in enumerate(blocks):
                if v[idx] == 1:
                    continue

                c_block = [x[:] for x in block]
                for _ in range(4):
                    if c_block == norm_place:
                        put_block(c_block, True)
                        answer += sum(sum(row) for row in c_block)
                        v[idx] = 1
                        matched = True
                        break
                    c_block = rotate_block(c_block)

                if matched:
                    break

        return answer
    
    def find_block(si, sj, v):
        q = deque()
        block = []
        
        q.append((si, sj))
        v[si][sj]=1
        block.append((si, sj))
        
        while q:
            ci, cj = q.popleft()
            
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci+di, cj+dj
                
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and table[ni][nj]==1:
                    q.append((ni, nj))
                    v[ni][nj]=1
                    block.append((ni, nj))
        return block
    
    
    def find_si_sj(target):
        si, sj = 1000, 1000
        for i, j in target:
            si = min(si, i)
            sj = min(sj, j)
        return si, sj
    
    def make_block(block):        
        si, sj = find_si_sj(block)
        norm_block = []
        for i, j in block:
            norm_block.append((i-si, j-sj))
        
        mx_i = max(i for i, j in norm_block)
        mx_j = max(j for i, j in norm_block)

        n_block = [[0]*(mx_j+1) for _ in range(mx_i+1)]
        
        for i, j in norm_block:
            n_block[i][j] = 1
            
        return n_block

    
    def print_block(block):
        for i in range(M):
            print(*block[i])
        print()
    
    def print_board():
        for i in range(N):
            print(*game_board[i])
        print()
    
    def rotate_block(block):
        row, col = len(block), len(block[0])
        rotated = [[0]*row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                rotated[j][row-i-1] = block[i][j]

        return rotated
    
    def find_board(si, sj, v):
        q = deque()
        block = []
        
        q.append((si, sj))
        v[si][sj]=1
        block.append((si, sj))
        
        while q:
            ci, cj = q.popleft()
            
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = ci+di, cj+dj
                
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and game_board[ni][nj]==0:
                    q.append((ni, nj))
                    v[ni][nj]=1
                    block.append((ni, nj))
                    
        return block
    
    def put_block(block, flag):
        block_loc = [(i, j) for i in range(len(block)) for j in range(len(block[0])) if block[i][j]==1]
        possible_place = []
        
        for i in range(N):
            for j in range(N):
                can_place = True
                for bi, bj in block_loc:
                    ni, nj = i+bi, j+bj
                    
                    if not (0<=ni<N and 0<=nj<N and game_board[ni][nj]==0):
                        can_place = False
                        break
                if can_place:
                    tmp = []
                    for bi, bj in block_loc:
                        ni, nj = i+bi, j+bj
                        tmp.append((ni, nj))
                        
                        if flag:
                            game_board[ni][nj]=5
                    
                    possible_place.append(tmp)
                    
        return possible_place   
        
                
    #-------------------------------------------------------
    
    # table에서 블록 찾기
    v = [[0]*N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if table[i][j]==1 and v[i][j]==0:
                block = find_block(i, j, v)
                blocks.append(make_block(block))
    # print(blocks)
    # print("----")
    
    v = [[0]*N for _ in range(N)]
    boards = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j]==0 and v[i][j]==0:
                board = find_board(i, j, v)
                boards.append(board)
    
    # print(boards)
    # print("----")
    
    answer = find_answer()
    
    
    return answer