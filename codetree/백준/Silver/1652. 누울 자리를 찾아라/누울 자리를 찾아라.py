N = int(input())
arr = []
for i in range(N):
    tmp = list(input())
    arr.append(tmp)

# print(arr)

row = col = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j]=='.':
            cnt += 1
        else:
            if cnt >= 2:
                row += 1
            cnt = 0
    if cnt >= 2:
        row += 1
print(row, end= ' ')

for j in range(N):
    cnt = 0
    for i in range(N):
        if arr[i][j]=='.':
            cnt += 1
        else:
            if cnt >= 2:
                col += 1
            cnt = 0
    if cnt >= 2:
        col += 1
print(col)