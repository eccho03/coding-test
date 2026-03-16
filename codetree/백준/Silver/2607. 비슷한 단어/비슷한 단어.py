from collections import Counter

# 비슷한 단어 조건
# 같은 종류 or 하나 더하거나 빼거나 바꾸었을 때 같은 경우
def check(word):
    word_cnt = Counter(word)
    target_word_cnt = Counter(target_word)
    # print(word_cnt, target_word_cnt)
    if len(word)==len(target_word):
        if word_cnt==target_word_cnt:
            return True
        else:
            # 하나의 문자를 바꿔서 되는지 확인
            tmp = target_word_cnt - word_cnt
            if len(dict(tmp)) == 1:
                tmp = dict(tmp)
                for v in tmp.values():
                    if v == 1:
                        return True
            else:
                return False

            return False
    elif len(word) < len(target_word):
        # 짧은 경우 - 하나의 문자를 더하기
        # DO DOG
        # GP SGP
        # KO KCO
        tmp = target_word_cnt-word_cnt
        if len(dict(tmp))==1:
            tmp = dict(tmp)
            for v in tmp.values():
                if v == 1:
                    return True
        else:
            return False

    else:
        # 긴 경우 - 하나의 문자를 빼기
        tmp = word_cnt - target_word_cnt
        if len(dict(tmp)) == 1:
            tmp = dict(tmp)
            for v in tmp.values():
                if v == 1:
                    return True
        else:
            return False

    return False

N = int(input())
target_word = input()
words = [input() for _ in range(N-1)]

# print(target_word)
# print(words)

cnt = 0
for word in words:
    if check(word):
        cnt += 1

print(cnt)