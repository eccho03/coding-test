import sys
input = sys.stdin.readline

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

S = input().strip()
q = int(input())
problems = [list(map(str, input().split())) for _ in range(q)]
# print(problems)
alpha = "abcdefghijklmnopqrstuvwxyz"

N = len(S)

alpha_cnt = []
for i in range(len(alpha)):
    arr = find_target(alpha[i])
    alpha_cnt.append(arr)

prefix_alpha_cnt = []
for i in range(len(alpha_cnt)):
    prefix_arr = sum_arr(alpha_cnt[i])
    prefix_alpha_cnt.append(prefix_arr)

# print(ord('c')-ord('a'))
for target, l, r in problems:
    l, r = int(l), int(r)
    #print(S[l:r+1])
    idx = ord(target)-ord('a')
    sys.stdout.write(str(prefix_alpha_cnt[idx][r+1]-prefix_alpha_cnt[idx][l])+'\n')