cnt = 0
def dfs(numbers,val,target, N, size):
    global cnt
    #print(val)
    if N==size-1:
        if val==target:
            cnt+=1
            #print(cnt)
        return cnt

    dfs(numbers,val-numbers[N+1],target, N+1, size)
    dfs(numbers,val+numbers[N+1],target, N+1, size)
    
    return cnt
    
def solution(numbers, target):
    global cnt
    answer = 0
    answer=dfs(numbers,numbers[0],target, 0, len(numbers))
    answer=dfs(numbers,-numbers[0],target, 0, len(numbers))
    return answer