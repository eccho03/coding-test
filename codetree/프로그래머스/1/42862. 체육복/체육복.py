def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = 0
    
    arr = [0 for _ in range(n)]
    
    for i in reversed(lost):
        if i in reversed(reserve):
            lost.remove(i)
            reserve.remove(i)
    # print(lost)
    # print(reserve)
    for i in range(1,n+1):
        if i not in lost:
            arr[i-1]=1
            
    for i in lost:
        for j in reserve:
            if j-1==i or j+1==i:
                reserve.remove(j)
                arr[i-1]=1
    answer = sum(arr)
    print(arr)
    
    return answer