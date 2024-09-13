import sys
input = sys.stdin.readline().rstrip()
input = input.split('-')
# print(input)

num = 0
tmp = []
output = []

for s in input:
    if "+" in s:
        tmp = s.split('+')
        tmp = list(map(int, tmp))

        for i in tmp:
            num += i
        output.append(str(num))
        num = 0
    else:
        output.append(s)

ans = int(output[0])
for s in output[1:]:
    ans -= int(s)

print(ans)

