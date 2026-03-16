from itertools import combinations

n, m = map(int, input().split())
city = []
house = []
chick = []

for _ in range(n):
    arr = list(map(int, input().split()))
    city.append(arr)

for i in range(len(city)):
    for j in range(len(city)):
        if city[i][j] == 1:
            house.append((i + 1, j + 1))
        elif city[i][j] == 2:
            chick.append((i + 1, j + 1))

chick_combi = list(combinations(chick, m))
min_dist = float('inf')

for k in chick_combi:
    cur_dist = 0
    for i in range(len(house)):
        dist = float('inf')
        for j in range(len(k)):
            x = abs(house[i][0] - k[j][0])
            y = abs(house[i][1] - k[j][1])
            dist = min(dist, (x + y))
        cur_dist += dist
    min_dist = min(min_dist, cur_dist)
print(min_dist)
