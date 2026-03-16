from itertools import combinations

arr = [int(input()) for _ in range(9)]

ans = []
for i in combinations(arr, 7):
    tlst = list(i)

    if sum(tlst)==100:
        ans = tlst
        break

ans.sort()

for i in ans:
    print(i)