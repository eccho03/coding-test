N = int(input())
candidate = [int(input()) for _ in range(N)]

if N==1:
    print(0)
else:
    # print(candidate)
    me = candidate[0] # 기호1번 = 다솜
    candidate = candidate[1:]
    ans = 0

    candidate.sort(reverse=True)

    while max(candidate)>=me:
        cur_max_idx = candidate.index(max(candidate))
        if me<=candidate[cur_max_idx]:
            me+=1
            candidate[cur_max_idx]-=1
            ans+=1

    print(ans)