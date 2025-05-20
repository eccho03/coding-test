from collections import deque

def is_pal(num):
    size = len(num)
    for i in range(size):
        if num[i]!=num[size-i-1]:
            return False

    return True

def bfs(X):
    q = deque()
    v = set()

    q.append((X, 0))
    v.add(X)

    while q:
        cur, cnt = q.popleft()

        #print(cur,cnt)

        if is_pal(bin(cur)[2:]):
            return cnt

        if cur+1 not in v:
            q.append((cur+1, cnt+1))
            v.add(cur+1)

        if cur>1 and cur-1 not in v:
            v.add(cur-1)
            q.append((cur-1, cnt+1))

T = int(input())
for _ in range(T):
    X = int(input())
    print(bfs(X))