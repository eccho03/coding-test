S = list(input())
ans = set()

for i in range(len(S)):
    tmp = ""
    for j in range(i,len(S)):
        tmp+=S[j]
        ans.add(tmp)

print(len(ans))