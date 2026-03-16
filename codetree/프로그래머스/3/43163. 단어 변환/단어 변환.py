from collections import deque
def solution(begin, target, words):
    answer = 0
    
    def bfs(begin,target):
        q = deque()
        v = set()
        
        q.append((begin,0))
        v.add(begin)
        
        while q:
            next,cnt = q.popleft()

            if next==target:
                return cnt
            
            for i in range(len(words)):
                if words[i] in v:   continue
                diff_cnt = 0
                for j in range(len(words[i])):
                    if words[i][j]!=next[j]:
                        diff_cnt+=1
                #print(diff_cnt,words[i],next)
                if diff_cnt==1:
                    q.append((words[i],cnt+1))
                    v.add(words[i])
                    cnt+=1
                    
        return 0

    if target not in words:
        answer = 0
    else:
        answer = bfs(begin,target)
    
    return answer