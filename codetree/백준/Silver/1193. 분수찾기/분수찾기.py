sum = 0
def find_diagonal(x):
    global sum
    idx = 1

    while True:
        sum += idx
        idx+=1
        if sum>=x:
            break
        #print(sum)
    return idx-1

# [1] 1+2+3+...+N >= X를 만족하는 N 구하기
X = int(input())
N = find_diagonal(X)
target_idx = 0
for i in range(sum-(N-1), sum+1):
    if i==X:
        break
    target_idx+=1
    #print(i, end=" ")

# print("start idx: ",target_idx)
# print("sum:",sum)
# print("N:",N)

si,sj=0,0
if N%2==0:  # 짝수 대각선
    si,sj=1,N
    for idx in range(target_idx):
        si,sj = si+1,sj-1
else:   # 홀수 대각선
    si,sj=N,1
    for idx in range(target_idx):
        si,sj = si-1,sj+1

print(f'{si}/{sj}')