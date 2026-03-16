X = input()
cnt = 0
ans = -1
while True:
    tmp = 0
    if 1<=int(X)<=9:
        ans = int(X)
        break
    for i in range(len(X)):
        tmp+=int(X[i])

    #print(tmp)
    cnt+=1
    X = str(tmp)
print(cnt)
if ans%3==0:
    print("YES")
else:
    print("NO")