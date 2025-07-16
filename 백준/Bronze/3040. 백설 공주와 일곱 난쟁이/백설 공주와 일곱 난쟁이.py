from itertools import combinations
arr = [int(input()) for _ in range(9)]
ans = []
for (ans) in combinations(arr, 7):
    if sum(ans)==100:
        ans = map(str, ans)
        break

print('\n'.join(ans))