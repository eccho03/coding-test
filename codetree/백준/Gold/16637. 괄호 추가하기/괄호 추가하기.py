from linecache import cache


def calculate(left, op, right):
    if op=='*':
        return left*right
    elif op=='+':
        return left+right
    else:
        return left-right

def dfs(idx, cur_val):
    global mx_ans
    if idx>=N:
        mx_ans = max(mx_ans, cur_val)
        return

    # 괄호 x
    if idx+2<=N:
        dfs(idx+2, calculate(int(cur_val), formula[idx], int(formula[idx+1])))

    # 괄호 o
    if idx+4<=N:
        gwalho = calculate(int(formula[idx+1]), formula[idx+2], int(formula[idx+3]))
        dfs(idx+4, calculate(int(cur_val), formula[idx], gwalho))

N = int(input())
formula = input().rstrip()
mx_ans = -float('inf')

dfs(1, int(formula[0]))
print(mx_ans)