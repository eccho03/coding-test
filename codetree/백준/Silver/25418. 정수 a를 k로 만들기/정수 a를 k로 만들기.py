from collections import deque
def bfs():
    q = deque()
    v = set()

    q.append((start, 0))
    v.add(start)

    while q:
        cur, cnt = q.popleft()

        if cur == end:
            return cnt

        for nxt in (cur+1, cur*2):
            if nxt not in v and 1<=nxt<=1_000_000:
                q.append((nxt, cnt+1))
                v.add(nxt)

start, end = map(int, input().split())

ans = bfs()
print(ans)