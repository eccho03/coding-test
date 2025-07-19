def dfs(start, end):
    global flag
    v[start]=1
    if start == end:
        flag=1
        return

    for i in graph[start]:
        if v[i]==0:
            dfs(i, end)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            graph[i+1].append(j+1)
            graph[j+1].append(i+1)

#print(graph)

plans = list(map(int, input().split()))

for i in range(len(plans)-1):
    flag=0
    v = [0] * (N+1)
    dfs(plans[i], plans[i+1])
    if flag==0:
        print("NO")
        exit()

print("YES")

