from collections import deque
def dfs(s):
    q = deque()

    q.append(s)
    v[s] = True
    cnt = 1
    #print(s, end=' ')

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not v[nxt]:
                v[nxt] = True
                cnt += 1
                q.append(nxt)
    return cnt

N,M = map(int,input().split())
num = [list(map(int,input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
mx_cnt = -1
ans = []

for a, b in num:
    graph[b].append(a)
#print(graph)

for i in range(1,N+1):
    v = [0] * (N + 1)
    cnt = dfs(i)
    if cnt == mx_cnt:
        ans.append(i)
    elif cnt > mx_cnt:
        mx_cnt = cnt
        ans.clear()
        ans.append(i)
print(*ans)