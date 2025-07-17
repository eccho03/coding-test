s = input().strip()
idx = 0
num = 1

while idx < len(s):
    str_num = str(num)

    for digit in str_num:
        if idx < len(s) and s[idx] == digit:
            idx += 1

    num += 1

print(num - 1)