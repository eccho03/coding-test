def func(num):
    hap = 0
    for i in range(len(num)):
        if num[i] in "0123456789":
            hap+=int(num[i])
    return hap

N = int(input())
serial = [input() for _ in range(N)]

serial.sort(key=lambda x:(len(x), func(x), x))

print('\n'.join(serial))