from itertools import combinations
from itertools import permutations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

init_start = [i for i in range(1, N+1)]

mn_diff = float('inf')

for num in range(1, N):
    for i in combinations(init_start, num):
        start = list(i)

        link = [x for x in init_start if x not in start]

        # print(start)
        # print(link)
        # print()

        cnt_start = 0
        for a, b in combinations(start, 2):
            cnt_start+=arr[a-1][b-1]
            cnt_start+=arr[b-1][a-1]

        cnt_link = 0
        for a, b in combinations(link, 2):
            cnt_link += arr[a-1][b-1]
            cnt_link += arr[b-1][a-1]

        mn_diff = min(mn_diff, abs(cnt_start-cnt_link))


print(mn_diff)