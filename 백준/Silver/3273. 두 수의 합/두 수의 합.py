N = int(input())
arr = list(map(int, input().split()))
X = int(input())
arr.sort()
cnt = 0
start, end = 0, N-1

while start < end:
    sum_two = arr[start]+arr[end] # 두 수의 합

    if sum_two > X:
        end -= 1
    elif sum_two == X:
        # print(arr[start], arr[end])
        cnt += 1
        start += 1
        end -= 1

    else:
        start += 1

print(cnt)
