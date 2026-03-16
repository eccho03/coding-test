candidate = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i!=j and j!=k and i!=k:
                candidate.append(str(i)+str(j)+str(k))

N=int(input())
for _ in range(N):
    num, strike, ball = map(int,input().split())
    num = str(num)
    tmp = []

    for j in range(len(candidate)):
        target = candidate[j]
        s, b = 0, 0 # strike, ball

        for k in range(3):
            if target[k]==num[k]:
                # 자리 같고, 숫자 같은 경우
                s += 1
            else:
                if num[k] in target:
                    b += 1
        #print(f'숫자: {target}, 스트: {s}, 볼: {b}')
        if s==strike and b==ball:
            tmp.append(target)

    candidate = tmp

    #print("------------------------")
print(len(candidate))