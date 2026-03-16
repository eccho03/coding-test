def mul(num):
    res = 1
    for i in range(len(num)):
        res *= int(num[i])
    return res

N = input()
size = len(N)

flag = 0

for i in range(1, size):
    left = mul(N[:i])
    right = mul(N[i:])
    # print(N[:i], N[i:])
    # print(left, right)
    if left == right:
        flag = 1
        break

if flag:
    print("YES")
else:
    print("NO")

