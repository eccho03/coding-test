def dfs(idx, cur_sum):
    global cnt
    if idx>=N:
        if cur_sum==S:
            cnt+=1
        return

    dfs(idx+1, cur_sum+arr[idx])
    dfs(idx+1, cur_sum)

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt=0
dfs(0, 0)

if S==0:
    cnt-=1
print(cnt)