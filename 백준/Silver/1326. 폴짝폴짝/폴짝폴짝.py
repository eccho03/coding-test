from collections import deque
def bfs(start):
    q = deque()
    v = set()

    q.append((start, 0))
    v.add(start)

    while q:
        cur, cnt = q.popleft()
        if cur==end:
            return cnt

        step = bridge[cur-1]
        nxt = cur + step

        while nxt<=N:
            if nxt not in v:
                q.append((nxt, cnt+1))
                v.add(nxt)
            nxt += step

        nxt = cur - step

        while nxt>=1:
            if nxt not in v:
                q.append((nxt, cnt+1))
                v.add(nxt)
            nxt -= step


    return -1


N = int(input())
bridge = list(map(int, input().split()))
start, end = map(int, input().split())

ans = bfs(start)
print(ans)