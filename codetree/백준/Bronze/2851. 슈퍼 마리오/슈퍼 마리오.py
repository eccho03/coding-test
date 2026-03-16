score = [int(input()) for _ in range(10)]
#print(score)

N=10
prefix = [0]*N
prefix[0]=score[0]

i=1
for i in range(1,N):
    prefix[i]=prefix[i-1]+score[i]

    if abs(prefix[i]-100)>=abs(prefix[i-1]-100):
        break

if abs(prefix[i-1]-100)<abs(prefix[i]-100):
    print(prefix[i-1])
else:
    print(prefix[i])