N, M = map(int, input().split())
days = [int(input()) for _ in range(N)]

start, end = max(days), sum(days)
K = 0  # 최소 인출 금액

while start <= end:
    mid = (start + end) // 2

    budget = 0  # 현재 남은 금액
    cnt = 1  # 최소 1번은 인출

    for today in days:
        if budget + today > mid:
            cnt += 1  # 인출
            budget = today
        else:
            budget += today  # 예산에 오늘의 지출을 더함

    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        K = mid

print(K)
