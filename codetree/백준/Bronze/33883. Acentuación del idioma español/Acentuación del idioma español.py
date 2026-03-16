S = input()
moeum = ['a','e','i','o','u']

ans = -1

# n, s & 자음으로 끝나는 단어 - 마지막 모음에 강세
if S[-1]!='n' and S[-1]!='s' and S[-1] not in moeum:
    #print("case1")
    for i in range(len(S)-1,-1,-1):
        if S[i] in moeum:
            #print(S[i])
            ans = i
            break
else:
    #print("case2")
    cnt = 0
    for i in range(len(S)-1,-1,-1):
        if S[i] in moeum:
            cnt+=1

        if cnt==2:
            #print(S[i])
            ans = i
            break

if ans!=-1:
    print(ans+1)
else:
    print(ans)