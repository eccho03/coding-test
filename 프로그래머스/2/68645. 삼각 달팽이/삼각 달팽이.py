def solution(n):
    answer = []
    triangle = []
    length=1
    for i in range(n):
        tmp = [0]*length
        length+=1
        triangle.append(tmp)
    # 3,3 -> 2,2 -> 1,1
    
    directions = [(1, 0), (0, 1), (-1, -1)]
    dir = 0
    num = 1
    ci, cj = 0, 0
    while num<=n*(n+1)//2:
        triangle[ci][cj] = num
        di, dj = directions[dir]
        
        ni, nj = ci+di, cj+dj
        if ni<0 or ni>=n or nj<0 or nj>ni or triangle[ni][nj]!=0:
            dir = (dir+1)%3
            di, dj = directions[dir]
            ni, nj = ci+di, cj+dj
        
        ci, cj = ni, nj
        num += 1
    
    # print(triangle)
    
    cnt=1
    for i in range(n):
        for j in range(cnt):
            answer.append(triangle[i][j])
        cnt+=1
    
    return answer