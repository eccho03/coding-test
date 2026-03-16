from collections import deque

N = int(input())
arr = []

# 모든 건물을 짓는 데 필요한 최소시간
# 배럭->벙커
# 여러 개 동시에 지을 수 있음

def topology():
    result = []
    q = deque()
    dp = [0]*(N+1)

    for i in range(1,N+1):
        if indegree[i]==0:
            dp[i] = time[i]
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for i in graph[cur]:
            indegree[i]-=1
            dp[i] = max(dp[i], dp[cur] + time[i])
            if indegree[i]==0:
                q.append(i)

    return dp


time = [0]*(N+1)

for i in range(N):
    tmp = list(map(int, input().split()))
    before = tmp[1:-1]
    time[i+1] = tmp[0]
    arr.append(before)

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for idx, before in enumerate(arr):
    for num in before:
        graph[num].append(idx+1)
        indegree[idx+1]+=1

# print(graph)
# print(indegree)

dp=topology()
for ans in dp[1:]:
    print(ans)