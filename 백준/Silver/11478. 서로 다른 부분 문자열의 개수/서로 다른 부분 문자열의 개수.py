from itertools import combinations

S = input()
N = len(S)
ans = set()

# for i in range(0,N):
#     print(S[i:i+1])
#
# for i in range(0,N):
#     print(S[i:i+2])
#
# for i in range(0,N):
#     print(S[i:i+3])
#
for i in range(N):
    for j in range(N):
        #print(S[i:i+j+1], end=' ')
        ans.add(S[i:i+j+1])
    #print()

#print(ans)
print(len(ans))