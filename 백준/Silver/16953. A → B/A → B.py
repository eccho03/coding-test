from collections import deque
def bfs(start, end):
    q = deque()
    v = set()

    q.append((start, 0))
    v.add(start)

    while q:
        cur, cnt = q.popleft()
        if cur==end:
            return cnt

        next1 = cur*2
        next2 = int(str(cur)+"1")

        for num in (next1,next2):
            if num<=end and num not in v:
                q.append((num, cnt+1))
                v.add(num)
    return -1


A, B = map(int, input().split())
ans = bfs(A,B)

if ans==-1:
    print(ans)
else:
    print(ans+1)

"""
num = 8
next1 = int(str(num)+"1")
print(next1)
"""