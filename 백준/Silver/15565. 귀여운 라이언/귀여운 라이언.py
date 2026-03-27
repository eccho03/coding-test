N, K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, N-1
cnt = 0
answer = float('inf')
for right in range(N):
    if arr[right]==1:
        cnt+=1

    while cnt>=K:
        answer = min(answer, right-left+1)

        if arr[left]==1:
            cnt-=1
        left+=1

if answer==float('inf'):
    print(-1)
else:
    print(answer)

