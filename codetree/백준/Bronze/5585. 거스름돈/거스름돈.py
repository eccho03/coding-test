money = [500, 100, 50, 10, 5, 1]
total = 1000
n = int(input())
my_money = total - n
res = 0
for i in money:
    res += my_money // i
    my_money %= i

print(res)