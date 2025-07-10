def find_target(target):
    arr = [0]*N
    for i in range(N):
        if S[i]==target:
            arr[i]=1
    return arr

def sum_arr(arr):
    prefix_arr = [0] * (N+1)
    for i in range(N):
        prefix_arr[i+1] = prefix_arr[i]+arr[i]

    return prefix_arr

S = input()
q = int(input())
problems = [list(map(str, input().split())) for _ in range(q)]
# print(problems)

N = len(S)

for target, l, r in problems:
    l, r = int(l), int(r)
    arr = find_target(target)
    prefix_arr = sum_arr(arr)
    # print(arr)
    # print(prefix_arr)
    print(prefix_arr[r+1]-prefix_arr[l])