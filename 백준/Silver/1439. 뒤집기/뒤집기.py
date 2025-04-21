# N=int(input())
# people = [list(map(int, input().split())) for _ in range(N)]
# print(people)
#
# people.sort(key=lambda x:(x[0],x[1]))
# print(people)
#
# ans = 0
#
# for idx in range(1,N):
#     prev1, prev2 = people[idx-1]
#     cur1, cur2 = people[idx]
#
#     if cur2>prev2:
#         pass
#     else: # cur2<prev2
#         print(idx)
#         ans+=1
# print(ans)

s = str(input())

sidx, eidx,tidx = -1,-1, -1
start = False
idx = 0
cnt_0, cnt_1 = 0,0
while True:
    # print(idx)
    if idx>=len(s)-1:
        if s[eidx-1]!=s[eidx]:
            if s[eidx]=="0":
                cnt_0+=1
            else:
                cnt_1+=1
        break

    if s[idx]=="0":
        cnt_0+=1
        sidx,eidx = idx,idx
        while True:
            if s[idx]=="1" or idx>=len(s)-1:
                break
            idx += 1
            eidx += 1
        #print("0:",sidx, eidx)

    elif s[idx]=="1":
        cnt_1 += 1
        sidx, eidx = idx,idx
        while True:
            if s[idx]=="0" or idx>=len(s)-1:
                break
            idx+=1
            eidx+=1
        #print("1:",sidx, eidx)
    idx = eidx
print(min(cnt_0, cnt_1))