N,M = map(int, input().split())
A=list(map(int,input().split()))

cur_sum = 0
cnt = 0
for start in range(N):
    cur_sum = A[start]

    if cur_sum==M:
        cnt+=1
        continue

    for i in range(start+1,N):
        cur_sum += A[i]
        if cur_sum==M:
            #print(start, i)
            cnt+=1
            break
        elif cur_sum>M:
            break
print(cnt)