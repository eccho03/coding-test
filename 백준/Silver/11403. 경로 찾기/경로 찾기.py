from collections import deque

def bfs(start, end):
    q = deque()
    v = [0] * N

    q.append(start)
    v[start] = 1

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not v[nxt]:
                if nxt == end:
                    return True
                v[nxt] = 1
                q.append(nxt)

            elif nxt == end:
                return True

    return False

def print_arr(arr):
    for row in arr:
        print(*row)
    print()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            graph[i].append(j)

# print(graph)

answer = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if bfs(i, j):
            answer[i][j]=1

print_arr(answer)