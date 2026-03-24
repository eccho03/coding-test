import math

def dfs(num, idx):
    if not sosu(int(num[:idx+1])):
        return False
    if idx==N-1:
        print(num)
        return True

    dfs(num+'1', idx+1)
    dfs(num+'2', idx+1)
    dfs(num+'3', idx+1)
    dfs(num+'5', idx+1)
    dfs(num+'7', idx+1)
    dfs(num+'9', idx+1)

def sosu(num):
    if num==1: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0: return False
    return True

N = int(input())

dfs('2', 0)
dfs('3', 0)
dfs('5', 0)
dfs('7', 0)