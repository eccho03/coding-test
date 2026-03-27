N, K = map(int, input().split())
arr = list(map(int, input().split()))

window = arr[:K]
mx_temp = sum(window)
temp = sum(window)

for i in range(K, N):
    prev = arr[i-K]
    nxt = arr[i]
    temp-=prev
    temp+=nxt

    mx_temp = max(mx_temp, temp)

print(mx_temp)
