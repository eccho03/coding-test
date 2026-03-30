def check_reduce(num, idx, size):
    global answer
    if idx==size-1:
        answer.append(int(num))
        return

    for i in range(0, 10):
        if int(num[idx])<=i: continue
        check_reduce(num+str(i), idx+1, size)


N = int(input())
cnt = 0
answer = []

for size in range(1, 11):
    for i in range(0, 10):
        check_reduce(str(i), 0, size)

# print(answer)
answer.sort()

if N<len(answer):
    print(answer[N])
else:
    print(-1)