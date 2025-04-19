def solution(tickets):
    answer = []
    tickets.sort()
    v = [0] * len(tickets)
    
    def dfs(cur, route):
        
        for i in range(len(tickets)):
            depart, dest = tickets[i]
            
            if len(route)==len(tickets)+1:
                answer.append(route)
                return
            
            if depart==cur and v[i]==0:
                v[i]=1
                dfs(dest, route+[dest])
                v[i]=0
            
    
    dfs("ICN",["ICN"])
    answer.sort()
    return answer[0]