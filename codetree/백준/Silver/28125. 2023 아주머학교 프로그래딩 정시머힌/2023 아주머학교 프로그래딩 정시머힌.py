change = {'@':'a', '[':'c', '!':'i', ';': 'j', '^':'n', '0': 'o', '7': 't', "\\\'": 'v', "\\\\'": 'w'}
N = int(input())
origin = [list(input()) for _ in range(N)]

# for i in range(N):
#     print(''.join(origin[i]))

#print(origin)

ans = [0] * N

for i in range(N):
    org = origin[i]
    for j in range(len(org)):
        if org[j] in change:
            org[j]=change[org[j]]
            ans[i] += 1

    for j in range(len(org)-1):
        #print(org[j]+org[j+1])
        if org[j]+org[j+1] in change:
            org[j] = change[org[j]+org[j+1]]
            ans[i] += 1
            #org.remove(org[j+1])


for i in range(N):
    num = ''.join(origin[i])
    num = num.replace("'", "")

    if '\\v' in num:
        num = num.replace('\\v', 'w')

    if len(num) <= ans[i] * 2:
        print("I don't understand")
    else:
        print(num)

#print(ans)