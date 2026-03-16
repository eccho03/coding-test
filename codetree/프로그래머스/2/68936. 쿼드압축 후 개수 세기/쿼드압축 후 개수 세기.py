def solution(arr):
    answer = [0, 0]
    N = len(arr)
    
    def dfs(si, sj, length):
        first = arr[si][sj]
        for i in range(si, si+length):
            for j in range(sj, sj+length):
                if arr[i][j]!=first:
                    length//=2
                    dfs(si+length, sj, length)
                    dfs(si, sj+length, length)
                    dfs(si+length, sj+length, length)
                    dfs(si, sj, length)
                    return
        answer[first]+=1
    
    dfs(0, 0, N)
    
    
    return answer