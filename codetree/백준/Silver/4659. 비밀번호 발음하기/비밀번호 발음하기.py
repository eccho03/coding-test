moeum = ['a', 'e', 'i', 'o', 'u']
while True:
    S = input()

    if S == "end":
        break

    flag = 0
    for i in moeum:
        if i in S:
            flag=1
            break
    if flag==0:
        #print("규칙 1 틀림")
        print(f'<{S}> is not acceptable.')
        continue

    streak_moeum = 0
    streak_jaeum = 0
    flag = 0
    for c in S:
        if c in moeum:
            streak_moeum+=1
            streak_jaeum=0
        else:
            streak_moeum=0
            streak_jaeum+=1

        if streak_moeum>=3 or streak_jaeum>=3:
            flag = 1
            break

    if flag==1:
        #print("규칙 2 틀림")
        print(f'<{S}> is not acceptable.')
        continue

    streak = 0
    flag = 0
    for i in range(len(S)-1):
        if S[i]==S[i+1] and S[i]!='e' and S[i]!='o':
            flag = 1

    if flag==1:
        print(f'<{S}> is not acceptable.')
        continue

    print(f'<{S}> is acceptable.')
