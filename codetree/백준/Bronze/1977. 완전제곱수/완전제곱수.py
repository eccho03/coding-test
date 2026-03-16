M = int(input())
N = int(input())

lst = []
if M<2:
    lst.append(1)
for i in range(1,N+1):
    for j in range(2, i):
        if i==(j*j) and i>=M:
            lst.append(i)

if len(lst)==0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))