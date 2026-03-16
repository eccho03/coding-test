from collections import defaultdict

def dfs(first_name, cur_name, cnt):
    global answer
    if cnt!=0:
        visited[cur_name]=1
    # print(cur_name, end=' ')
    if cnt!=0 and first_name==cur_name:
        answer+=1
        return

    for i in graph[cur_name]:
        if visited[i]==0:
            dfs(first_name, i, cnt+1)


TC = 1
while True:
    N = int(input())
    cur_input = list(map(str, input().split()) for _ in range(N))
    names = []
    graph = defaultdict(list)
    name_lst = set()

    if N==0:
        break

    for a, b in cur_input:
        graph[a].append(b)
        name_lst.add(a)
        name_lst.add(b)

    # print(graph)
    # print(name_lst)
    visited = {}
    for init in name_lst:
        visited[init] = 0

    answer = 0
    for name in name_lst:
        if visited[name]==0:
            dfs(name, name, 0)
            # print()

    print(TC, answer)
    TC+=1
