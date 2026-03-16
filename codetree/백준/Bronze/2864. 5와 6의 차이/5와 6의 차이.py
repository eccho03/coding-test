A, B = map(str, input().split())

mx_A, mx_B = '', ''
mn_A, mn_B = '', ''
for i in range(len(A)):
    if A[i]=='5':
        mx_A+='6'
    else:
        mx_A+=A[i]

    if B[i]=='5':
        mx_B+='6'
    else:
        mx_B+=B[i]

for i in range(len(A)):
    if A[i]=='6':
        mn_A+='5'
    else:
        mn_A+=A[i]

    if B[i]=='6':
        mn_B+='5'
    else:
        mn_B+=B[i]

print(int(mn_A)+int(mn_B), int(mx_A)+int(mx_B))
