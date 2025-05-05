while True:
    flag = 0
    S = input()
    if S=='0':
        break

    for i in range(len(S)):
        if S[i]!=S[len(S)-i-1]:
            flag = 1

    if flag==1:
        print("no")
    else:
        print("yes")