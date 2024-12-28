import sys
sys.setrecursionlimit(10**6)

def dfs(g, x, y, alpha):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if (g[x][y] == alpha):
        g[x][y] = 0
        dfs(g, x-1, y, alpha)
        dfs(g, x, y-1, alpha)
        dfs(g, x+1, y, alpha)
        dfs(g, x, y+1, alpha)
        return True
    
    return False

n = int(input())
graph = []

origin = dict()
origin['red'] = 0
origin['green'] = 0
origin['blue'] = 0

color = dict()
color['red'] = 0
color['green'] = 0
color['blue'] = 0

for _ in range(n):
    graph.append(list(map(str, input())))

color_graph = [row[:] for row in graph]
for i in range(n):
    for j in range(n):
        if color_graph[i][j] == 'R':
            color_graph[i][j] = 'G'


for i in range(n):
    for j in range(n):
        if dfs(graph, i, j, 'R') == True:
            origin['red'] += 1
        elif dfs(graph, i, j, 'G') == True:
            origin['green'] += 1 
        elif dfs(graph, i, j, 'B') == True:
            origin['blue'] += 1 
        
        if dfs(color_graph, i, j, 'R') == True:
            color['red'] += 1
        elif dfs(color_graph, i, j, 'G') == True:
            color['green'] += 1 
        elif dfs(color_graph, i, j, 'B') == True:
            color['blue'] += 1 

print(origin['red'] + origin['green'] + origin['blue'], color['red'] + color['green'] + color['blue'])