n = int(input())
res = 0
alpha_cnt = [0 * 26 for _ in range(26)]
# alpha_cnt = [0] * 26

for i in range(n):
    word = input()
    group_word = True

    for j in range(len(word)):
        if j > 0 and word[j] != word[j - 1]:
            if alpha_cnt[ord(word[j]) - 97] > 0:
                group_word = False
                break
        alpha_cnt[ord(word[j]) - 97] += 1

    if group_word:
        res += 1
    alpha_cnt = [0] * 26
    
print(res)
