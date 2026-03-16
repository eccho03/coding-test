from collections import deque

def bfs(v):

    queue =  deque()
    queue.append(v)
    distance[v] = 0

    while queue:
        n = queue.popleft()
        
        if n == k:
            return distance[n]
        
        t = [n-1, n+1, 2*n]

        for i in range(3):
            if t[i] < 0 or t[i] >= len(distance):
                continue

            if distance[t[i]] == -1:
                distance[t[i]] = distance[n] + 1
                queue.append(t[i])

n, k = map(int, input().split())
distance = [-1] * 100001
answer = bfs(n)
print(answer)