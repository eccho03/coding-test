each = 0
arr = []
def dfs(x, y):
    global each
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    # 해당 좌표 아직 방문 x
    if graph[x][y] == 1:
        graph[x][y] = 0 # 방문 처리
        each += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

n = int(input())
graph =[]
for _ in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            arr.append(each)
            each = 0

print(result)
arr.sort()
for i in arr:
    print(i)