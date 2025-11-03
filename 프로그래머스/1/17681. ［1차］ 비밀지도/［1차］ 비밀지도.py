def solution(n, arr1, arr2):
    answer = []
    
    map1 = []
    map2 = []
    
    new_arr = [[0]*n for _ in range(n)]
    
    for i in range(n):
        cur_line1 = format(arr1[i], f'0{n}b')
        cur_line2 = format(arr2[i], f'0{n}b')
        map1.append(list(map(int, cur_line1)))
        map2.append(list(map(int, cur_line2)))
        
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = map1[i][j]|map2[i][j]
    
    for i in range(n):
        tmp = ""
        for j in range(n):
            if new_arr[i][j]==1:
                tmp+='#'
            else:
                tmp+=' '
        answer.append(tmp)
    
    return answer