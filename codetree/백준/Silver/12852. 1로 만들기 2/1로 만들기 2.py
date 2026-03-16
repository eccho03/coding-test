from collections import deque
def bfs(start):
    q = deque()
    v = set()

    q.append((start,0,[start]))
    v.add(start)

    while q:
        cur, cnt, path = q.popleft()
        if cur==1:
            return path,cnt

        next1,next2=-1,-1
        if cur%3==0:
            next1 = cur//3
        if cur%2==0:
            next2 = cur//2
        next3 = cur-1

        for node in (next1,next2,next3):
            if node>=1 and node not in v:
                q.append((node,cnt+1,path+[node]))
                v.add(node)

    return -1 # 도달할 리는 없는 곳

N=int(input())
path,cnt = bfs(N)
print(cnt)
print(*path)