S = input().rstrip()

cnt_0, cnt_1 = 0, 0

for ch in S:
    if ch == '1':
        cnt_1 += 1
    elif ch == '0':
        cnt_0 += 1

cnt_0, cnt_1 = cnt_0//2, cnt_1//2
# print(cnt_0, cnt_1)

print('0'*cnt_0+'1'*cnt_1)