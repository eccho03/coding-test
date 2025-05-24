N = int(input())
M = int(input())
S = input()
P = "IO"

Pn = P*N+"I"
#print(Pn)
ans = 0

for i in range(M):
    #print(i, i+len(Pn))
    if i+len(Pn)>M:
        break
    #print(S[i:i+len(Pn)])
    if S[i:i+len(Pn)] == Pn:
        #print(Pn)
        ans+=1
print(ans)