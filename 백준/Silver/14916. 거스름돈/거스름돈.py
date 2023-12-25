cnt = 0

money = int(input())
flag = 0

while money != 1 and money != 0:
    while money >= 5:
        money -= 5
        cnt += 1
        flag = 1

    while money >= 2:
        money -= 2
        cnt += 1

    if money != 0 and flag == 1:
        money += 5
        cnt -= 1

        while money >= 2:
            money -= 2
            cnt += 1

if money == 0:
    print(cnt)
else:
    print("-1")