from itertools import combinations

N = int(input())
cards = [list(map(int, input().split())) for _ in range(N)]
mx_num = [0]*N
for i in range(N):
    card = cards[i]
    for j in combinations(card, 3):
        #print(sum(j))
        mx_num[i] = max(mx_num[i], sum(j)%10)

#print(max(mx_num))

for i in range(N-1, -1, -1):
    if mx_num[i]==max(mx_num):
        print(i+1)
        break