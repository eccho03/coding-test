N, K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
cnt = 0
answer = float('inf')

while right < N:
    if arr[right] == 1:
        cnt += 1

    while cnt >= K:
        answer = min(answer, right - left + 1)

        if arr[left] == 1:
            cnt -= 1
        left += 1

    right += 1

print(answer if answer != float('inf') else -1)