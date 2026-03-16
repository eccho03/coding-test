def solution(rows, columns, queries):
    answer = []
    
    def print_arr(arr):
        max_val = max(max(row) for row in arr)
        width = len(str(max_val))

        for row in arr:
            for val in row:
                print(str(val).rjust(width), end="  ")
            print()

    
    def move(arr, si, sj, ei, ej):
        cpy_arr = [x[:] for x in arr]
        tmp = arr[si][ej]
        mn_val = float('inf')
        
        # 우
        for j in range(sj, ej):
            cpy_arr[si][j+1]=arr[si][j]
            mn_val = min(mn_val, arr[si][j])
        # print_arr(cpy_arr)
                
        # 하
        for i in range(si, ei):
            cpy_arr[i+1][ej]=arr[i][ej]
            mn_val = min(mn_val, arr[i][ej])
        
        # 좌
        for j in range(sj, ej):
            cpy_arr[ei][j]=arr[ei][j+1]
            mn_val = min(mn_val, arr[ei][j+1])
            
        # 상
        for i in range(si, ei):
            cpy_arr[i][sj]=arr[i+1][sj]
            mn_val = min(mn_val, arr[i+1][sj])
        
        # print_arr(cpy_arr)
        
        return cpy_arr, mn_val 
        
    
    arr = [[0]*columns for _ in range(rows)]
    narr = [x[:] for x in arr]
    
    num=1
    for i in range(rows):
        for j in range(columns):
            arr[i][j]=num
            num+=1
    
    # print_arr(arr)
    
    
    ###test
    for query in queries:
        x1,y1,x2,y2 = query
        narr, mn_val = move(arr, x1-1, y1-1, x2-1, y2-1)
        # print_arr(narr)
        # print(mn_val)
        # print("--------")
        arr=narr
        answer.append(mn_val)
    
    
    
    return answer