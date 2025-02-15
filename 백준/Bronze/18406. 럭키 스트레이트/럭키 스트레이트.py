import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, str(n)))

t = len(num)

left= 0
right = 0

for i in range(t//2):
    left += num[i]

for i in range(t//2, t):
    right += num[i]

if left == right:
    print("LUCKY")
else:
    print("READY")