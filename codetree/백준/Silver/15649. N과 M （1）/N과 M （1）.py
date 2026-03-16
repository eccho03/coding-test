def permu(arr, n):
    res = []
    if n>len(arr):
        return res
    if n==1:
        for i in arr:
            res.append([i])
    elif n>1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in permu(ans,n-1):
                res.append([arr[i]]+p)
    return res

N,M = map(int, input().split())

arr=[i+1 for i in range(N)]
ans = permu(arr, M)
for i in ans:
    print(*i)