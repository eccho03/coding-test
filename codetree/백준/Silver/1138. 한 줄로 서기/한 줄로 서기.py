N=int(input())
arr=list(map(int,input().split()))
orders=[]
for i in range(N-1,-1,-1):
    num=arr[i]
    orders.insert(num,i+1)

print(*orders)