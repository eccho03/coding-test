import math

N = int(input())

def check(num):
    if num==1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def dfs(num, idx):

    if idx==N:
        print(num)
        return

    # print(num[:idx+1])
    for d in range(10):
        nxt = num*10+d

        if check(nxt)==True:
            dfs(nxt, idx+1)

for i in (2,3,5,7):
    dfs(i, 1)