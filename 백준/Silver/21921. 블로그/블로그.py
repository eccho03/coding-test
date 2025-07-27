N, X = map(int, input().split())
days = list(map(int, input().split()))

sum_days = [0]*(N+1)

for i in range(N):
    sum_days[i+1] = sum_days[i] + days[i]
# print(sum_days)

mx_visit = 0
for i in range(0,N-X+1):
    # print(sum_days[X+i]-sum_days[i])
    mx_visit = max(mx_visit, sum_days[X+i]-sum_days[i])

cnt = 0
for i in range(0,N-X+1):
   if mx_visit == sum_days[X+i]-sum_days[i]:
       cnt += 1

if mx_visit == 0:
    print("SAD")
else:
    print(mx_visit)
    print(cnt)