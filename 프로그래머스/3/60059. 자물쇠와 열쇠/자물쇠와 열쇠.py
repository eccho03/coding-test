def rotate(key):
    return [list(reversed(c)) for c in zip(*key)]

def create_new(lock, k):
    l = len(lock)
    n = l + 2 * (k - 1)
    new = [[0] * n for _ in range(n)]
    
    for i in range(l):
        for j in range(l):
            new[i + k - 1][j + k - 1] = lock[i][j]
    
    return new

def attach(board, key, x, y):
    k = len(key)
    for i in range(k):
        for j in range(k):
            board[x+i][y+j] += key[i][j]

def detach(board, key, x, y):
    k = len(key)
    for i in range(k):
        for j in range(k):
            board[x+i][y+j] -= key[i][j]
            
def check_unlock(board, l, k):
    offset = k - 1
    for i in range(l):
        for j in range(l):
            if board[i+offset][j+offset] != 1:
                return False
    return True

def solution(key, lock):
    l = len(lock)
    k = len(key)
    board = create_new(lock, k)
    
    for _ in range(4):
        key = rotate(key)
        
        for x in range(len(board) - k + 1):
            for y in range(len(board) - k + 1):
                attach(board, key, x, y)
                if check_unlock(board, l, k):
                    return True
                detach(board, key, x, y)
            
    return False