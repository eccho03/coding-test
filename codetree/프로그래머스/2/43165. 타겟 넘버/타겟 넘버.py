cnt = 0
def dfs(numbers, val, target, N, size):
    global cnt
    if N == size - 1:
        if val == target:
            cnt += 1
        return
    dfs(numbers, val - numbers[N + 1], target, N + 1, size)
    dfs(numbers, val + numbers[N + 1], target, N + 1, size)

def solution(numbers, target):
    global cnt
    cnt = 0 
    dfs(numbers, numbers[0], target, 0, len(numbers))
    dfs(numbers, -numbers[0], target, 0, len(numbers))
    return cnt