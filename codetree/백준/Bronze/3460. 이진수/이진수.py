T = int(input())
for _ in range(T):
    n = int(input())
    num= []
    while n>0:
        if n%2 == 1:  # 나머지가 1이면 출력
            num.append(1)
        else:
            num.append(0)
        n=n//2

    for i in range(len(num)):
        if num[i]==1:
            print(i, end=' ')