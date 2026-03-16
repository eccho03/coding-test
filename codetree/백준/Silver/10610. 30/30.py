num = list(input())

if '0' not in num or sum(map(int, num))%3!=0:
    print(-1)
else:
    num.sort(reverse=True)
    print(''.join(num))