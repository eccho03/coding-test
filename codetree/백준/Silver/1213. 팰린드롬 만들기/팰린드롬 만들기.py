from collections import defaultdict, OrderedDict

S = input().strip().upper()

alpha_cnt = defaultdict(int)
for ch in range(len(S)):
    alpha_cnt[S[ch]] += 1

sorted_alpha_cnt = OrderedDict()
for ch in sorted(alpha_cnt.keys()):
    sorted_alpha_cnt[ch] = alpha_cnt[ch]

# print(sorted_alpha_cnt)

holsu = ""
flag = True
ans = ""

for i in sorted_alpha_cnt.items():
    alpha, cnt = i
    # print(alpha, cnt)

    if cnt%2==1:
        if holsu=="":
            holsu += alpha
        else:
            flag = False
            break

for i in sorted_alpha_cnt.items():
    alpha, cnt = i
    ans += alpha * (cnt//2)

if not flag:
    print("I'm Sorry Hansoo")
else:
    print(ans+holsu+ans[::-1])