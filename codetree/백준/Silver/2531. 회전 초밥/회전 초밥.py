N, d, k, c = list(map(int, input().split()))
dishes = [int(input()) for _ in range(N)]

cnt = 0

mx_val = 0

window = dishes[0:k-1]
for i in range(N):
    window.append(dishes[(i+k-1)%N])
    # print(window)
    mx_val = max(mx_val, len(set(window+[c])))

    window.pop(0)

print(mx_val)