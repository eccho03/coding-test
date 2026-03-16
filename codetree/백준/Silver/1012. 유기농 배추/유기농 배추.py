import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

result =[]
T = int(input())
for _ in range(T):
    bug = 0
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                bug += 1

    result.append(bug)

for i in result:
    print(i)