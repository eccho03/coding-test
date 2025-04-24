N=int(input())

kg5 = 0
kg3 = 0

while N>0:
    if N%5==0:
        N -= 5
        kg5+=1

    else:
        kg3+=1
        N-=3

if N==0:
    print(kg3+kg5)
else:
    print(-1)