from collections import deque
def solution(n, computers):
    answer = 0
    
    graph = [[] * (n+1) for _ in range((n+1))]
    
    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j]==1:
                graph[i+1].append(j+1)
    #print(graph)
    
    v = [0] * (n+1)
    
    def bfs(start):
        q = deque([start])
        v[start] = True

        while q:
            cur = q.popleft()
            #print(cur, end=' ')
            for i in graph[cur]:
                if not v[i]:
                    q.append(i)
                    v[i] = True
                    
    
    for i in range(1,n+1):
        if v[i]==0:
            bfs(i)
            answer+=1
        
    return answer