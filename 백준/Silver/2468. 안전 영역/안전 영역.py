import sys
sys.setrecursionlimit(10**6)

def dfs(h, x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if temp_graph[x][y] > h and temp_graph[x][y] != 0:
        temp_graph[x][y] = 0
        dfs(h, x-1, y)
        dfs(h, x, y-1)
        dfs(h, x+1, y)
        dfs(h, x, y+1)
        return True
    
    return False

n = int(input())
graph = []
max_height = 0
for i in range(n):
    graph.append(list(map(int, input().split(' '))))
    max_height = max(graph[i])
# print(max_height)

max_safe = 0
cur_safe = 0
ans = []
for k in range(max_height + 1):
    temp_graph = [row[:] for row in graph]
    cur_safe = 0
    for i in range(n):
        for j in range(n):
            if dfs(k, i, j) == True:
                cur_safe += 1
    if max_safe < cur_safe: 
        max_safe = cur_safe

print(max_safe)