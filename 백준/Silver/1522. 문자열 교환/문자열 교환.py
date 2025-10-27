def cnt_s(s, target):
    cnt = 0
    for t in s:
        if t == target:
            cnt += 1
    return cnt

s = input().strip()

new_s = s+s
# print(new_s)
cnt_a = cnt_s(s, 'a')
mn_cnt = float('inf')

for i in range(len(s)):
    window = new_s[i:i+cnt_a]
    mn_cnt = min(mn_cnt, cnt_s(window, 'b'))

    # print(window)
print(mn_cnt)