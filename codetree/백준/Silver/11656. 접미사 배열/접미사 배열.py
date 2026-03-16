S = input()

ans = []

for i in range(len(S)):
    tmp =""
    for j in range(i, len(S)):
        tmp+=S[j]

    ans.append(tmp)

ans.sort()

print('\n'.join(ans))