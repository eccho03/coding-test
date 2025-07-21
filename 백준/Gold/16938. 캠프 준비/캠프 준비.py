from itertools import combinations

'''
문제 N개, i번째 문제 난이도: Ai
개수 - 문제 2문제 이상 사용
난이도 - L<=합<=R , 가장 어려운 난이도 문제 - 가장 쉬운 난이도 문제 >= X
-> 캠프에 사용할 문제 고르는 방법의 수
'''

def check_difficulty(arr):
    sum_arr = 0
    for i in arr:
        sum_arr += difficulty[i-1]
    return sum_arr

def check_balance(arr):
    diff_arr = set()
    for i in arr:
        diff_arr.add(difficulty[i-1])

    mx_diff, mn_diff = max(diff_arr), min(diff_arr)

    return mx_diff, mn_diff

N, L, R, X = map(int, input().split())
difficulty = list(map(int, input().split()))
num = [i for i in range(1,N+1)]
ans = 0

for i in range(2, N+1):
    for j in combinations(num, i):
        # print(j)
        sum_diff = check_difficulty(j)
        mx_diff, mn_diff = check_balance(j)
        # print(f'합: {sum_diff}, 최대값: {mx_diff}, 최소값: {mn_diff}')

        if L<=check_difficulty(j)<=R:
            mx_diff, mn_diff = check_balance(j)
            if mx_diff-mn_diff >= X:
                # print("ans: ",j)
                ans+=1

print(ans)