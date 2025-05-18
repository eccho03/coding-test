from itertools import combinations

N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

def is_valid(subjects):
    seen = set()
    total = 0
    for sub in subjects:
        credit, cnt = int(sub[0]), int(sub[1])
        for j in range(2, len(sub), 2):
            day, hour = sub[j], int(sub[j+1])
            if (day, hour) in seen:
                return 0
            seen.add((day, hour))
        total += credit
    return total

mx_credit = 0
for i in range(1, N + 1):
    for narr in combinations(arr, i):
        credit = is_valid(narr)
        if credit > mx_credit:
            mx_credit = credit

if mx_credit >= M:
    print("YES")
else:
    print("NO")