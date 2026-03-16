from collections import defaultdict

N,M = map(int,input().split())
words = [input() for _ in range(N)]
target_words = [w for w in words if len(w)>=M] # 길이가 M 이상인 단어들만 남겨놓기

word_cnt = defaultdict(int)

for word in target_words:
    word_cnt[word]+=1

# 1. 빈도(1) - 내림 // 2. 길이(0) - 내림 // 3. 알파벳순(0) - 오름
count_words = sorted(word_cnt.items(),key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in count_words:
    print(word[0])