from collections import deque
def bfs(s):
    q = deque()
    v = [0] * (N+1)

    q.append(s)
    v[s] = 1
    cnt = 1

    while q:
        cur = q.popleft()

        for nxt in (cur+stone[cur], cur-stone[cur]):
            if 1<=nxt<=N and v[nxt] == 0:
                q.append(nxt)
                v[nxt] = 1
                cnt+=1
    return cnt

N = int(input())
stone = [0]+list(map(int, input().split()))
start = int(input())

ans = bfs(start)
print(ans)

# print(stone)