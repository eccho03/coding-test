N, M = map(int, input().split())
days = list(map(int, input().split()))

profit = days[:M]

cur_benefit = sum(profit)
mx_benefit = sum(profit)

for i in range(M, N):
    prev = days[i-M]
    nxt = days[i]

    cur_benefit-=prev
    cur_benefit+=nxt

    mx_benefit = max(mx_benefit, cur_benefit)

print(mx_benefit)
