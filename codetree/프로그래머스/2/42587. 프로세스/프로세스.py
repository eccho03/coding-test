from collections import deque
def solution(priorities, location):
    ans = []
    N = len(priorities)
    num = [i for i in range(N)]
    # print(num)
    
    q = deque()
    for n in num:
        q.append(n)
    
    idx = 0
    while q:
        cur = q.popleft()
        
        if any(priorities[cur] < priorities[i] for i in q):
            q.append(cur)
        else:
            ans.append(cur)
    
    #print(ans)
    answer = ans.index(location)+1
    
    
    return answer