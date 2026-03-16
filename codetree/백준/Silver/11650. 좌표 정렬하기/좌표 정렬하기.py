import sys

n = int(sys.stdin.readline().rstrip())
coordinate = []

for i in range(n):
    coo = list(map(int, sys.stdin.readline().rstrip().split()))
    coordinate.append(coo)

coordinate.sort(key=lambda x: (x[0], x[1]))

for i in coordinate:
    print(i[0], i[1])