N = int(input())
num = list(input().split())

order = {'B': 1, 'S': 2, 'G': 3, 'P': 4, 'D': 5}
flag = 0

before = [(diff[0], int(diff[1:])) for diff in num]
#print(before)

after = sorted(before, key=lambda x: (order[x[0]], -x[1]))
#print(after)

if before==after:
    print("OK")
else:
    print("KO")
    for i in range(N):
        if before[i] != after[i]:
            print(f"{after[i][0]}{after[i][1]} {before[i][0]}{before[i][1]}")
            break