import sys

n = int(sys.stdin.readline().rstrip())
a = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

for i in b:
    if i in a:
        print("1", end=' ')
    else:
        print("0", end=' ')
