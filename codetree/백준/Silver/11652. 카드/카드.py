from collections import defaultdict

N = int(input())
cards = [int(input()) for _ in range(N)]
card_cnt = defaultdict(int)

for card in cards:
    card_cnt[card] += 1

max_count = max(card_cnt.values())

most_frequent = [card for card, count in card_cnt.items() if count == max_count]
print(min(most_frequent))