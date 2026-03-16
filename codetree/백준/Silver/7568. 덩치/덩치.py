n = int(input())
arr = [[0, 0] for i in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    arr[i][0] = x
    arr[i][1] = y
res = [1] * n


for i in range(n):
    for j in range(n):
        if arr[i][1] < arr[j][1] and arr[i][0] < arr[j][0]:
            res[i] += 1

for i in range(n):
    print(res[i], end=' ')


