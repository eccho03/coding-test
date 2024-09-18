coins = [25, 10, 5, 1]
coin = 0
res = [0 * 4 for _ in range(4)]
tmp = 0
T = int(input())
arr = [0 * T for _ in range(T)]
for i in range(T):
    arr[i] = int(input())

idx = 0
for i in range(T):
    coin = arr[i]
    for i in coins:
        res[idx] += coin // i
        coin %= i
        idx += 1
    for i in range(4):
        print(res[i], end=' ')
        idx = 0
    res = [0 * 4 for _ in range(4)] 
    print("")