import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

listen = set()
watch = set()

for i in range(n):
    listen.add(sys.stdin.readline().rstrip())
for i in range(m):
    watch.add(sys.stdin.readline().rstrip())

lis_and_wat = list(listen & watch)

lis_and_wat.sort()

print(len(lis_and_wat))
for i in lis_and_wat:
    print(i)