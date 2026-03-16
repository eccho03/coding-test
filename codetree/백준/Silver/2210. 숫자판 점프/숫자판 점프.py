def dfs(si, sj, cnt, num):
    if cnt==5:
        # print(int(num))
        ans.add(int(num))
        return

    for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
        ni, nj = si+di, sj+dj

        if ni<0 or ni>=5 or nj<0 or nj>=5:
            continue
        dfs(ni, nj, cnt+1, num+str(arr[ni][nj]))


arr = [list(map(int, input().split())) for i in range(5)]
# print(arr)
v = [[0]*5 for _ in range(5)]

ans = set()

for si in range(5):
    for sj in range(5):
        dfs(si, sj, 0, str(arr[si][sj]))


print(len(ans))