N, C = map(int, input().split())
M = int(input())
info = [list(map(int, input().split())) for _ in range(M)]

# 마을 도착지 순으로 정렬 (먼저 내릴 수록 우선순위 높음)
info.sort(key=lambda x: (x[1], x[0]))

# 트럭 상태: 마을 간 도착지별 적재량
truck = [0] * (N+1)
ans = 0

for i in range(M):
    send, receive, amount = info[i]
    available = C
    for j in range(send, receive):
        available = min(C-truck[j], available)

    tmp = min(amount, available)
    for j in range(send, receive):
        truck[j] += tmp

    ans += tmp

print(ans)
