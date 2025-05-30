from collections import deque
def bfs():
    q = deque()
    v = set()

    q.append((N, 0))
    v.add(N)

    while q:
        cur, cnt = q.popleft()

        if cur==M:
            return cnt

        for nxt in (cur+1, cur-1, cur+A, cur+B, cur-A, cur-B, cur*A, cur*B):
            if nxt not in v and 0<=nxt<=100_000:
                q.append((nxt, cnt+1))
                v.add(nxt)

    return -1 # 도달할 리는 없는 곳..


A, B, N, M = map(int, input().split())

ans = bfs()
print(ans)