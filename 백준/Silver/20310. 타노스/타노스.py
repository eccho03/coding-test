S = input().rstrip()

cnt_0, cnt_1 = S.count('0')//2, S.count('1')//2

tmp = []
for ch in S:
    # 앞에서부터 1 제거
    if ch == '1' and cnt_1 > 0:
        cnt_1 -= 1
    else:
        tmp.append(ch)

ans = []
# print(tmp)
for ch in reversed(tmp):
    # 뒤에서부터 0 제거
    if ch == '0' and cnt_0 > 0:
        cnt_0 -= 1
    else:
        ans.append(ch)

print(''.join(reversed(ans)))