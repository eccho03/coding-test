from collections import defaultdict

N = int(input())

files = [input() for _ in range(N)]
extend_cnt = defaultdict(int)

for file in files:
    tmp, extend = file.split('.')
    extend_cnt[extend]+=1

sort_extend = sorted(list(extend_cnt.items()))

for ex in sort_extend:
    print(ex[0], ex[1])
