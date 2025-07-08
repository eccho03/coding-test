A, B = map(str, input().split())
N = len(B)
mn_diff = float('inf')

for i in range(len(B)-len(A)+1):
    diff=0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            diff+=1
    mn_diff = min(mn_diff, diff)

print(mn_diff)
