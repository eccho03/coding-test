def solution(n, w, num):
    def find_coordinate(num):
        for i in range(h):
            for j in range(w):
                if boxes[i][j]==num:
                    return i, j
    
    answer = 0
    
    h = (n+w-1) // w
    
    boxes = [[0]*w for _ in range(h)]
    
    # 우상좌상
    directions = [(0,1),(-1,0),(0,-1),(-1,0)]
    dir = 0
    cnt = 1
    flag = 0
    for col in range(h-1,-1,-1):
        if flag==0:
            for row in range(w):
                if cnt>n:   break
                boxes[col][row]=cnt
                cnt+=1
            flag=1
        else:
            for row in range(w-1,-1,-1):
                if cnt>n:   break
                boxes[col][row]=cnt
                cnt+=1
            flag=0
    
    ti, tj = find_coordinate(num)
    
    # print(boxes)
    # print(ti, tj)
    
    for i in range(h):
        # print(boxes[i][tj])
        if boxes[i][tj]!=0:
            answer+=1
        if boxes[i][tj]==num:
            break
        
    return answer