from collections import deque

# 0-1 bfs
def bfs(start, end):
    q = deque()
    v = [-1] * 100001

    q.append((start, 0))
    v[start] = 0

    while q:
        cur, cnt = q.popleft()
        if cur == end:
            return cnt

        # 순간이동: 0초
        if 0 <= cur*2 <= 100000 and v[cur*2] == -1:
            q.appendleft((cur*2, cnt))
            v[cur*2] = cnt

        # 일반 이동: 1초
        for n in (cur-1, cur+1):
            if 0 <= n <= 100000 and v[n] == -1:
                q.append((n, cnt + 1))
                v[n] = cnt+1

    return 0

N, K = map(int, input().split())
ans = bfs(N, K)
print(ans)