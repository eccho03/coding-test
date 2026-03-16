document = input()
target = input()

idx = 0
start = target[0]

cnt = 0

while True:
    if idx>len(document)-len(target):
        break
    if document[idx]==start:
        flag = 1

        #print(document[idx])
        for j in range(1,len(target)):
            if idx+j >= len(document) or j>=len(target):
                break
            if document[idx+j]!=target[j]:
                flag = 0
                break

        if flag==1:
            idx+=len(target)
            cnt+=1
        else:
            idx+=1
    else:
        idx+=1

print(cnt)