def dfs(idx, sum):
    global cnt
    if idx == N:
        return

    sum += num[idx]
    if sum==S:
        cnt+=1
    dfs(idx+1, sum)
    dfs(idx+1, sum-num[idx])



N,S=map(int,input().split())
num = list(map(int,input().split()))
cnt = 0
dfs(0, 0)
print(cnt)