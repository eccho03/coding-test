N = int(input())
weights = [int(input()) for _ in range(N)]
weights.sort(reverse=True)

w=1
mx_weight = 0
for i in range(N):
    mx_weight = max(mx_weight, weights[i]*(i+1))

print(mx_weight)
