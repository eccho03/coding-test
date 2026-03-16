def solve(s):
    for i in range(len(s)):
        if s[i]=='U':
            for j in range(i+1,len(s)):
                if s[j]=='C':
                    for k in range(j+1,len(s)):
                        if s[k]=='P':
                            for l in range(k+1,len(s)):
                                if s[l]=='C':
                                    return True
    return False


S = input()
tmp = ""
for i in range(len(S)):
    if S[i].isupper():
        tmp += S[i]


if not solve(tmp):
    print("I hate UCPC")
else:
    print("I love UCPC")