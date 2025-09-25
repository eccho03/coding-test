from itertools import combinations

def dfs(start):
    global flag

    v[start]=1
    # print(start, end=' ')
    tmp.add(start)
    if start in truth_arr:
        flag = False
        return

    for i in graph[start]:
        if v[i]==0:
            dfs(i)

N, M = map(int, input().split())
truth_arr = list(map(int, input().split()))
trust_num = truth_arr[0]
truth_arr = set(truth_arr[1:])
party = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
for i in range(M):
    party[i] = party[i][1:]
    for j in combinations(party[i], 2):
        # print(j)
        n1, n2 = j
        graph[n1].append(n2)
        graph[n2].append(n1)

# print(graph)
ans = 0
for i in range(M):
    v = [0]*(N+1)
    # print("----")
    tmp = set()
    flag = True
    dfs(party[i][0])
    # print(flag)
    if not flag:
        for num in tmp:
            truth_arr.add(num)
    else:
        tmp.clear()
        ans+=1
    # print(truth_arr)

print(ans)