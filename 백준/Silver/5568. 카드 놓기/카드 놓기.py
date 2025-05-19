from itertools import permutations

N = int(input())
K = int(input())
card = [int(input()) for _ in range(N)]

#print(card)

lst = set()

for i in permutations(card, K):
    num = list(i)
    lst.add(''.join(map(str, num)))

print(len(lst))