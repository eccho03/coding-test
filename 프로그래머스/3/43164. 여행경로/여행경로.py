from collections import deque
def solution(tickets):
    answer = []
    tickets.sort()
    
    def bfs(start, sroute, used):
        q = deque()
        q.append((start, sroute, used))
        
        while q:
            cur, croute, cused = q.popleft()
            
            if len(cused)==len(tickets):
                answer.append(croute)
                continue
            
            for idx in range(len(tickets)):
                snode, enode = tickets[idx]
                #print(snode, enode)
                
                if snode == cur and idx not in cused:
                    q.append((enode, croute+[enode], cused+[idx]))
            
        return []
    
    bfs("ICN", ["ICN"], [])
    answer.sort()
            
    return answer[0]