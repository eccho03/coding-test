time = [300, 60, 10]
T = int(input())
origin = T
tmp = 0
res = [0, 0, 0]
sum = 0

for i in range(3):
    tmp = T // time[i]
    T %= time[i]
    res[i] = tmp
    sum += res[i] * time[i]


if (sum == origin):
    print(res[0], res[1], res[2], end=' ')
else:
    print("-1")
