def solution(wallpaper):
    answer = []
    N,M = len(wallpaper),len(wallpaper[0])
    arr = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j]=='#':
                arr[i][j]=1
    
    si, sj, ei, ej = 0,0,0,0
    
    for i in range(N):
        if sum(arr[i])>0:
            si=i
            break
    for i in range(N-1,-1,-1):
        if sum(arr[i])>0:
            ei=i
            break
    
    for j in range(M):
        tmp = 0
        for i in range(N):
            tmp+=arr[i][j]
        if tmp!=0:
            sj=j
            break
    for j in range(M-1,-1,-1):
        tmp = 0
        for i in range(N):
            tmp+=arr[i][j]
        if tmp!=0:
            ej=j
            break
        
    # print(si,sj,ei,ej)
    
    return [si,sj,ei+1,ej+1]