def solution(n, computers):
    answer = 0
    
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    
    def union(a,b):
        a=find(a)
        b=find(b)
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
    
    parent = [0]*(n)
    
    for i in range(n):
        parent[i]=i
    
    for i in range(n):
        for j in range(n):
            if i==j:continue
            if computers[i][j]==1:
                union(i, j)
    
    ans_arr=set()
    for i in range(n):
        root = find(i)
        ans_arr.add(root)
    
    return len(ans_arr)