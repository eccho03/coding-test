from collections import defaultdict

def dfs(n):
    v.add(n)
    tmp.append(n)
    # print(n, end=' ')

    for i in graph[n]:
        if i not in v:
            dfs(i)

    return tmp

N = int(input())
q = [list(map(str, input().split())) for _ in range(N)]
M = int(input())
a = [list(map(str, input().split())) for _ in range(M)]

# print(q)
# print(a)

graph = defaultdict(list)

for n1, _, n2 in q:
    graph[n1].append(n2)

# print(graph)

all_ans = dict()

for num in list(graph.keys()):
    v = set()
    tmp = []
    ans = dfs(num)
    # print(ans)
    # print()

    all_ans[num] = set(ans)

# print(all_ans)

for n1, _, n2 in a:
    if n1 in all_ans and n2 in all_ans[n1]:
        print('T')
    else:
        print('F')
