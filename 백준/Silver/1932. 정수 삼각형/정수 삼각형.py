n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

d = [[0] * n for _ in range(n)]
d[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            d[i][j] = arr[i][j] + d[i-1][j]
        elif j == len(arr[i])-1:
            d[i][j] = arr[i][j] + d[i-1][j-1]
        else:
            d[i][j] = arr[i][j] + max(d[i-1][j-1], d[i-1][j])
print(max(d[n-1]))