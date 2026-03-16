def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x]!=x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a,b):
        a=find(a)
        b=find(b)
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
    
    costs.sort(key=lambda x: x[2]) # cost 기준 정렬
    for i in range(len(costs)):
        a, b, cost = costs[i]
        if find(a)!=find(b):
            union(a, b)
            answer += cost
    
    
    return answer