# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
# def div(a, b):
#     if a < 0 and b > 0:
#         # 음수를 양수로 나눌 때
#         a = abs(a)
#         return -(a // b)
#     else:
#         return a // b


def dfs(idx, result, add, sub, mul, div):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    if add:
        dfs(idx + 1, result + num[idx], add - 1, sub, mul, div)
    if sub:
        dfs(idx + 1, result - num[idx], add, sub - 1, mul, div)
    if mul:
        dfs(idx + 1, result * num[idx], add, sub, mul - 1, div)
    if div:
        if result < 0 and num[idx] > 0:
            # 음수를 양수로 나눌 때
            result = abs(result)
            dfs(idx + 1, -(result // num[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, result // num[idx], add, sub, mul, div - 1)

n = int(input())

num = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

max_val = -float('inf')
min_val = float('inf')

dfs(1, num[0], add, sub, mul, div)
print(max_val)
print(min_val)