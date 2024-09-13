n = int(input())
cnt = 0
num = 1
while True:
    cnt += num
    if (cnt > n):
        break
    num += 1

print(num - 1)