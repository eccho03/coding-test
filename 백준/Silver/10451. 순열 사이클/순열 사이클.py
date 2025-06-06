def dfs(num, start):
    global ans
    v[num]=1

    if num==start and v[num]==1:
        ans += 1

    # print(num, end=' ')
    for i in graph[num]:
        if v[i]==0:
            dfs(i, start)

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sarr = [i for i in range(1,N+1)]
    graph = [[] for _ in range(N+1)]

    # print(sarr)
    # print(arr)

    for i in range(N):
        # 단방향 그래프
        graph[sarr[i]].append(arr[i])

    v = [0] * (N + 1)
    ans = 0

    for i in range(1,N+1):

        if v[i]==0:
            dfs(i, i)
            # print()

    print(ans)