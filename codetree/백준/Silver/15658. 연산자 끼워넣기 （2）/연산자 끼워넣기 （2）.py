from itertools import permutations

def dfs(val, idx, plus,minus,mul,div):
    global mx_val, mn_val
    if idx==N-1:
        mx_val = max(mx_val, val)
        mn_val = min(mn_val, val)
        #print(val)
        return

    if plus:
        dfs(val+A[idx+1], idx+1, plus-1, minus, mul, div)
    if minus:
        dfs(val-A[idx+1], idx+1, plus, minus-1, mul, div)
        #dfs(cur_oper, val, idx+1)
    if mul:
        dfs(val*A[idx+1],idx+1,plus, minus, mul-1, div)
        #dfs(cur_oper, val, idx+1)
    if div:
        #음수를 양수로 나눌 때
        if val<0 and A[idx]>0:
            dfs(-(abs(val)//A[idx+1]), idx+1, plus, minus, mul, div-1)
        else:
            dfs(val//A[idx+1],idx+1, plus, minus, mul, div-1)
        #dfs(cur_oper, val, idx+1)

N = int(input())
A = list(map(int, input().split()))
cnt = list(map(int, input().split()))

mx_val, mn_val = -float('inf'), float('inf')
dfs(A[0], 0, cnt[0],cnt[1],cnt[2],cnt[3])
#print(cnt)
print(mx_val)
print(mn_val)