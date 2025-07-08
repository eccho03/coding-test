arr = []
size = []
for i in range(5):
    tmp = input()
    arr.append(tmp)
    size.append(len(tmp))

idx=0
while True:
    if idx==max(size):
        break

    for i in range(5):
        if size[i]>idx:
            print(arr[i][idx], end='')
    idx+=1