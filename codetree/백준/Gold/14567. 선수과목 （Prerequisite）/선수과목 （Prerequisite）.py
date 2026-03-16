from collections import deque

def topology():
    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i]==0:
            q.append((i, 1))
            answer[i]='1'

    while q:
        cur, idx = q.popleft()
        result.append(cur)

        for i in graph[cur]:
            indegree[i]-=1
            if indegree[i]==0:
                answer[i]=str(idx+1)
                q.append((i, idx+1))

N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
answer = [0]*(N+1)

for a, b in conditions:
    graph[a].append(b)
    indegree[b]+=1

topology()
print(' '.join(answer[1:]))