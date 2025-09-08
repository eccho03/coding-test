def permu(arr, cur, k):
    if len(arr)==k:
        print(''.join(arr))
        return
    prev = None
    for i in range(k):
        if v[i]==0 and prev != letters[cur][i]:
            v[i]=1
            arr.append(letters[cur][i])
            permu(arr, cur, len(letters[cur]))
            v[i]=0
            arr.pop()
            prev = letters[cur][i]

N = int(input())
letters = [list(input().rstrip()) for _ in range(N)]

for i in range(N):
    M = len(letters[i])
    v=[0]*M
    letters[i].sort()
    lst = []
    permu([], i, M)
