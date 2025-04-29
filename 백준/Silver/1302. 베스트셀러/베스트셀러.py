import collections
title_cnt = collections.defaultdict(int)

N=int(input())
titles = [input() for _ in range(N)]

for title in titles:
    title_cnt[title]+=1

max_title = [k for k,v in title_cnt.items() if max(title_cnt.values())==v]
max_title.sort()
print(max_title[0])