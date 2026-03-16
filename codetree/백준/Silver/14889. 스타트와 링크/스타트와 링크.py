def dfs(depth, idx):
    global result
    if depth == n // 2:
        start_team, link_team = 0, 0
        start, link = [], []

        for i in range(n):
            if visited[i]:
                start.append(i)
            else:
                link.append(i)

        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                start_team += s[start[i]][start[j]] + s[start[j]][start[i]]
                link_team += s[link[i]][link[j]] + s[link[j]][link[i]]

        result = min(result, abs(start_team - link_team))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
result = float('inf')
visited = [False] * n

dfs(0, 0)
print(result)
