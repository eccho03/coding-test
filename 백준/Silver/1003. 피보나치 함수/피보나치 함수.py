T = int(input())
for _ in range(T):
    n = int(input())
    zero = [0] * 41
    one = [0] * 41
    for i in range(0, 41):
        if i == 0:
            zero[i] += 1
        elif i == 1:
            one[i] += 1
        else:
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
    print(zero[n], one[n])